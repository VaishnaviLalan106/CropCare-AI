import os
import sys
from PIL import Image

sys.path.insert(0, os.path.abspath("CropCare_AI"))
from model import load_model, predict_image
from disease_info import get_disease_info

def run_tests():
    print("Testing Model Loading...")
    model, processor, err = load_model()
    if err:
        print(f"Error: {err}")
        return False
    print("Model loaded successfully.")

    sample_dir = "CropCare_AI/samples"
    for fname in sorted(os.listdir(sample_dir)):
        fpath = os.path.join(sample_dir, fname)
        img = Image.open(fpath)
        preds = predict_image(img, model, processor, top_k=3)
        top1 = preds[0]
        info = get_disease_info(top1["class_name"])
        print(f"\n--- Testing Sample: {fname} ---")
        print(f"Image Size: {img.size}, Mode: {img.mode}")
        print(f"Top 1: {top1['display_name']} | Confidence: {top1['percentage']}")
        print(f"Status: {info['status']} | Severity: {info['severity']}")
        print(f"Top 2: {preds[1]['display_name']} ({preds[1]['percentage']})")
        print(f"Top 3: {preds[2]['display_name']} ({preds[2]['percentage']})")
        print(f"Sample Treatment: {info['treatment'][0]}")

    print("\nAll End-to-End tests passed successfully!")
    return True

if __name__ == "__main__":
    success = run_tests()
    sys.exit(0 if success else 1)
