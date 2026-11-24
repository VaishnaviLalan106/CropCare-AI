# 🌿 CropCare AI – Plant Disease Identification System

An intelligent, CNN-powered agricultural decision support application designed for fast, accurate plant disease identification and treatment recommendations.

CropCare AI uses a pretrained MobileNetV2 architecture (`neghani/plantvillage-mobilenetv2`) trained on the PlantVillage dataset covering **38 distinct plant health classes** across 14 major agricultural crop species.

---

## 🌟 Key Features

1. **Agriculture Green Modern UI:**
   - Professional, responsive white and natural green theme.
   - Clean card-based layout with visual feedback, status badges, and styled progress bars.
2. **Plant Leaf Image Upload & Preview:**
   - Supports JPG, JPEG, and PNG formats.
   - Live image preview with pixel dimensions, aspect ratio, and color mode verification.
   - Built-in demonstration sample leaves for instant testing during presentations.
3. **Genuine CNN Classification:**
   - Powered by `neghani/plantvillage-mobilenetv2`.
   - Top-3 predicted classes returned with genuine softmax confidence percentages.
4. **Agronomic Care & Disease Knowledge:**
   - Complete profiles for all 38 classes: symptoms, causal pathogens, favorable conditions, curative treatments, and preventative measures.
   - Downloadable diagnostic agronomy report slip.
5. **Session Dashboard & History:**
   - Live counters for total scans, healthy vs. diseased foliage, and average confidence.
   - Tabular history log with clear/reset options.
6. **Comprehensive Knowledge Base:**
   - Searchable and filterable reference library for all 38 plant diseases.

---

## 📁 Project Directory Structure

```text
CropCare_AI/
│
├── app.py                # Streamlit web interface and dashboard
├── model.py              # CNN model loader and genuine inference engine
├── disease_info.py       # Knowledge base for all 38 PlantVillage classes
├── requirements.txt      # Project dependencies
├── README.md             # Documentation and presentation guide
│
└── samples/              # Preloaded sample leaf images for instant demo
    ├── apple_healthy.jpg
    ├── tomato_early_blight.jpg
    └── corn_common_rust.jpg
```

---

## 🚀 How to Run the Application

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Launch the Streamlit App
From the `CROP_PROJECT` workspace root:
```bash
streamlit run CropCare_AI/app.py
```
Or, if navigating inside `CropCare_AI`:
```bash
cd CropCare_AI
streamlit run app.py
```

The application will open automatically in your browser at `http://localhost:8501`.

---

## 🧠 Model Specifications

- **Hugging Face Model ID:** `neghani/plantvillage-mobilenetv2`
- **Architecture:** MobileNetV2 for Image Classification
- **Classes:** 38 PlantVillage classes (Apple, Blueberry, Cherry, Corn, Grape, Orange, Peach, Pepper, Potato, Raspberry, Soybean, Squash, Strawberry, Tomato)
- **Input Resolution:** 224 × 224 RGB tensors
- **Preprocessing:** Bilinear resize to 256 shortest edge, center crop to 224, normalized with mean `[0.5, 0.5, 0.5]` and std `[0.5, 0.5, 0.5]`.

---

## 🎯 Internship Presentation Quick Demo Tips

1. Launch `streamlit run CropCare_AI/app.py`.
2. In the **Plant Disease Diagnosis** section:
   - Click the **"🍅 Tomato (Early Blight)"** or **"🍎 Apple (Healthy)"** sample button.
   - Click **"Run Plant Disease Diagnosis"**.
   - Show the **Top 3 predictions** with genuine confidence scores.
   - Switch between the **Symptoms & Causes**, **Treatment Plan**, and **Prevention** tabs.
   - Click **"Download Diagnostic Agronomy Slip"** to demonstrate report generation.
3. Navigate to **"📊 Analytics Dashboard"** to show real-time scan statistics and history tracking.
4. Navigate to **"📖 Disease Knowledge Base"** to filter conditions by crop (e.g., Tomato, Corn).
