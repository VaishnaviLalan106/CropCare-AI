"""
model.py - Optimized Model Loader and Inference Engine
Handles loading the pretrained Hugging Face CNN model (neghani/plantvillage-mobilenetv2),
module-level caching, failure-handling without repeated download retries,
and high-performance genuine forward-pass inference.
"""

import os
import hashlib
from typing import Tuple, List, Dict, Any, Optional
from PIL import Image
import torch

try:
    from transformers import AutoImageProcessor, AutoModelForImageClassification
    TRANSFORMERS_AVAILABLE = True
except ImportError:
    TRANSFORMERS_AVAILABLE = False


MODEL_ID = "neghani/plantvillage-mobilenetv2"

# Module-level singletons to prevent repeated disk I/O and network requests
_CACHED_MODEL = None
_CACHED_PROCESSOR = None
_LOAD_ATTEMPTED = False
_LOAD_ERROR: Optional[str] = None

# In-memory inference cache: {image_hash: list_of_predictions}
_INFERENCE_CACHE: Dict[str, List[Dict[str, Any]]] = {}


def is_transformers_installed() -> bool:
    """Check if transformers and torch are installed."""
    return TRANSFORMERS_AVAILABLE


def reset_model_cache() -> None:
    """Reset cached model state to allow manual reload/retry if desired."""
    global _CACHED_MODEL, _CACHED_PROCESSOR, _LOAD_ATTEMPTED, _LOAD_ERROR, _INFERENCE_CACHE
    _CACHED_MODEL = None
    _CACHED_PROCESSOR = None
    _LOAD_ATTEMPTED = False
    _LOAD_ERROR = None
    _INFERENCE_CACHE.clear()


def load_model(
    model_name: str = MODEL_ID,
    force_reload: bool = False
) -> Tuple[Optional[Any], Optional[Any], Optional[str]]:
    """
    Load the pretrained model and image processor with singleton caching.
    
    Guarantees:
    1. If already loaded in memory, returns immediately in ~0.0ms.
    2. If a previous load attempt failed, returns the cached error immediately
       without repeatedly attempting network connections or retrying failed downloads.
    3. First attempts offline cache (local_files_only=True) to avoid any network latency.
    4. Falls back to remote download exactly once if not cached.

    Returns:
        (model, processor, error_message)
    """
    global _CACHED_MODEL, _CACHED_PROCESSOR, _LOAD_ATTEMPTED, _LOAD_ERROR

    if force_reload:
        reset_model_cache()

    # 1. Return cached model in-memory immediately if already loaded
    if _CACHED_MODEL is not None and _CACHED_PROCESSOR is not None:
        return _CACHED_MODEL, _CACHED_PROCESSOR, None

    # 2. If previous attempt failed, fail-fast without re-running failed network calls
    if _LOAD_ATTEMPTED and _LOAD_ERROR is not None:
        return None, None, _LOAD_ERROR

    if not TRANSFORMERS_AVAILABLE:
        _LOAD_ATTEMPTED = True
        _LOAD_ERROR = "The 'transformers' or 'torch' package is not installed."
        return None, None, _LOAD_ERROR

    _LOAD_ATTEMPTED = True

    try:
        # First attempt fast offline loading from local huggingface cache
        try:
            processor = AutoImageProcessor.from_pretrained(model_name, local_files_only=True)
            model = AutoModelForImageClassification.from_pretrained(model_name, local_files_only=True)
            model.eval()
            _CACHED_MODEL = model
            _CACHED_PROCESSOR = processor
            _LOAD_ERROR = None
            return _CACHED_MODEL, _CACHED_PROCESSOR, None
        except Exception:
            # Fall back to single download attempt
            processor = AutoImageProcessor.from_pretrained(model_name)
            model = AutoModelForImageClassification.from_pretrained(model_name)
            model.eval()
            _CACHED_MODEL = model
            _CACHED_PROCESSOR = processor
            _LOAD_ERROR = None
            return _CACHED_MODEL, _CACHED_PROCESSOR, None

    except Exception as exc:
        _LOAD_ERROR = (
            f"Failed to load model '{model_name}'. Error: {type(exc).__name__}: {str(exc)}\n"
            "Network download failed. System is in fail-fast mode to prevent repeated network delays."
        )
        return None, None, _LOAD_ERROR


def compute_image_hash(image: Image.Image) -> str:
    """Compute a fast MD5 digest of an image's raw bytes to detect repeated inputs."""
    return hashlib.md5(image.tobytes()).hexdigest()


def predict_image(
    image: Image.Image,
    model: Any,
    processor: Any,
    top_k: int = 3,
    use_cache: bool = True
) -> List[Dict[str, Any]]:
    """
    Perform genuine model inference on an input PIL image with caching.

    If use_cache is True and the exact image has already been processed,
    returns the cached prediction list in ~0.0ms, skipping tensor conversion,
    normalization, and CNN forward pass.
    """
    if model is None or processor is None:
        raise ValueError("Model or processor is not loaded.")

    # Check inference cache by image hash
    img_hash = None
    if use_cache:
        img_hash = f"{compute_image_hash(image)}_{top_k}"
        if img_hash in _INFERENCE_CACHE:
            return _INFERENCE_CACHE[img_hash]

    # 1. Ensure image is in RGB mode
    if image.mode != "RGB":
        image = image.convert("RGB")

    # 2. Preprocess the image using the model's genuine processor requirements
    inputs = processor(images=image, return_tensors="pt")

    # 3. Model forward pass with disabled gradient computation
    with torch.no_grad():
        outputs = model(**inputs)
        logits = outputs.logits

        # Compute genuine softmax probabilities across all 38 classes
        probs = torch.nn.functional.softmax(logits, dim=-1)[0]

        # Extract top-k probabilities and indices
        effective_k = min(top_k, probs.shape[-1])
        top_probs, top_indices = torch.topk(probs, effective_k)

    results = []
    id2label = getattr(model.config, "id2label", {})

    for rank, (p, idx) in enumerate(zip(top_probs, top_indices), start=1):
        class_idx = idx.item()
        raw_class_name = id2label.get(class_idx, id2label.get(str(class_idx), f"Class_{class_idx}"))
        prob_float = float(p.item())

        parts = raw_class_name.split("___")
        plant = parts[0].replace("_", " ").title() if len(parts) > 0 else "Plant"
        condition = parts[1].replace("_", " ").title() if len(parts) > 1 else "Condition"
        display_name = f"{plant} - {condition}"
        is_healthy = "healthy" in raw_class_name.lower()

        results.append({
            "rank": rank,
            "class_idx": class_idx,
            "class_name": raw_class_name,
            "display_name": display_name,
            "plant": plant,
            "condition": condition,
            "probability": prob_float,
            "percentage": f"{prob_float * 100:.2f}%",
            "is_healthy": is_healthy
        })

    # Store in memory cache
    if use_cache and img_hash is not None:
        _INFERENCE_CACHE[img_hash] = results

    return results


def get_model_info(model: Any) -> Dict[str, Any]:
    """Retrieve metadata about the loaded model."""
    if model is None:
        return {"loaded": False, "model_id": MODEL_ID}

    id2label = getattr(model.config, "id2label", {})
    return {
        "loaded": True,
        "model_id": MODEL_ID,
        "architecture": getattr(model.config, "architectures", ["MobileNetV2"])[0],
        "num_classes": len(id2label),
        "classes": list(id2label.values())
    }
