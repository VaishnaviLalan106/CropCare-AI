import os
import sys
import time
from PIL import Image

sys.path.insert(0, os.path.abspath("CropCare_AI"))
import model as crop_model
import disease_info as crop_disease

def benchmark():
    print("=" * 60)
    print("CropCare AI Performance & Caching Benchmark")
    print("=" * 60)

    # 1. Benchmark Model Loading
    crop_model.reset_model_cache()
    
    t0 = time.perf_counter()
    m1, p1, err1 = crop_model.load_model()
    t_initial_load = time.perf_counter() - t0
    assert err1 is None, f"Initial load failed: {err1}"
    print(f"[1] Initial Model Load Time (from disk/cache): {t_initial_load:.4f} s")

    t0 = time.perf_counter()
    m2, p2, err2 = crop_model.load_model()
    t_cached_load = time.perf_counter() - t0
    print(f"[2] Cached Model Load Time (singleton memory):   {t_cached_load * 1000:.4f} ms")
    speedup_model = (t_initial_load / max(t_cached_load, 1e-9))
    print(f"    --> Model Caching Speedup: {speedup_model:,.1f}x faster")

    # 2. Benchmark Inference & Image Deduplication
    sample_img_path = "CropCare_AI/samples/tomato_early_blight.jpg"
    test_img = Image.open(sample_img_path)

    # Clear inference cache
    crop_model._INFERENCE_CACHE.clear()

    t0 = time.perf_counter()
    res1 = crop_model.predict_image(test_img, m2, p2, top_k=3, use_cache=True)
    t_first_infer = time.perf_counter() - t0
    print(f"\n[3] First Image Inference Time (CNN forward pass): {t_first_infer * 1000:.2f} ms")
    print(f"    Top-1: {res1[0]['display_name']} ({res1[0]['percentage']})")

    t0 = time.perf_counter()
    res2 = crop_model.predict_image(test_img, m2, p2, top_k=3, use_cache=True)
    t_cached_infer = time.perf_counter() - t0
    print(f"[4] Repeated Image Inference Time (Cached Hash):   {t_cached_infer * 1000:.4f} ms")
    speedup_infer = (t_first_infer / max(t_cached_infer, 1e-9))
    print(f"    --> Image Processing Avoidance Speedup: {speedup_infer:,.1f}x faster")

    # 3. Benchmark Disease Information Caching
    crop_disease.get_disease_info.cache_clear()
    
    t0 = time.perf_counter()
    d1 = crop_disease.get_disease_info("Tomato___Early_blight")
    t_first_db = time.perf_counter() - t0
    
    t0 = time.perf_counter()
    d2 = crop_disease.get_disease_info("Tomato___Early_blight")
    t_cached_db = time.perf_counter() - t0
    print(f"\n[5] First Disease Info Lookup:  {t_first_db * 1000:.4f} ms")
    print(f"[6] Cached Disease Info Lookup: {t_cached_db * 1000:.6f} ms")
    speedup_db = (t_first_db / max(t_cached_db, 1e-9))
    print(f"    --> Disease Info Cache Speedup: {speedup_db:,.1f}x faster")

    # 4. Benchmark Fail-Fast Model Error Handling (no endless retry loops)
    t0 = time.perf_counter()
    bad_m, bad_p, bad_err = crop_model.load_model("invalid_nonexistent_model_id", force_reload=True)
    t_fail_first = time.perf_counter() - t0
    
    t0 = time.perf_counter()
    bad_m2, bad_p2, bad_err2 = crop_model.load_model("invalid_nonexistent_model_id", force_reload=False)
    t_fail_cached = time.perf_counter() - t0
    print(f"\n[7] Initial Failure Detection Time:  {t_fail_first:.4f} s")
    print(f"[8] Cached Fail-Fast Response Time:   {t_fail_cached * 1000:.4f} ms (no repeated download retry!)")

    print("\n" + "=" * 60)
    print("Summary of Measured Results:")
    print(f"  • Model Reloading Overhead Eliminated: {t_initial_load:.2f}s -> {t_cached_load * 1000:.3f}ms")
    print(f"  • Repeated Image Processing Avoided:   {t_first_infer * 1000:.1f}ms -> {t_cached_infer * 1000:.3f}ms")
    print(f"  • Static Disease Lookup Cached:        {t_cached_db * 1000:.4f}ms")
    print(f"  • Failure Handling: Fail-Fast in       {t_fail_cached * 1000:.3f}ms")
    print("=" * 60)

if __name__ == "__main__":
    benchmark()
