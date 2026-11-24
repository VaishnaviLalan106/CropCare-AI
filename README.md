# 🌱 CropCare AI – AI-Powered Plant Disease Identification System

**An intelligent plant disease identification application powered by Deep Learning and Convolutional Neural Networks (CNN).**

CropCare AI helps users identify potential plant diseases by uploading leaf images. It uses a pretrained MobileNetV2 image classification model to analyze the uploaded image and provide disease predictions, confidence scores, and general crop care recommendations.

## 🚀 Live Application

**[🌐 Try CropCare AI – Live Demo](https://vaishnavilalan106-cropcare-ai-cropcare-aiapp-f6zwyi.streamlit.app/)**

## 📌 Project Overview

Plant diseases can affect crop quality and agricultural productivity. Early identification can help farmers and plant enthusiasts take appropriate preventive measures.

CropCare AI provides a simple web-based interface where users can upload a plant leaf image and receive AI-based classification results.

The application uses a pretrained deep learning model rather than training a CNN from scratch.

## ✨ Key Features

- **Plant Image Upload:** Upload leaf images in JPG, JPEG, and PNG formats.
- **AI-Based Disease Detection:** Classifies plant leaf images using a pretrained MobileNetV2 CNN model.
- **Top 3 Predictions:** Displays the three most likely classification results.
- **Confidence Scores:** Shows the model's prediction confidence for each class.
- **Disease Information:** Provides information about symptoms, causes, and disease characteristics.
- **Crop Care Recommendations:** Displays general treatment and prevention suggestions.
- **Analytics Dashboard:** Tracks prediction activity and disease counts.
- **Disease Knowledge Base:** Provides disease-related reference information.
- **Downloadable Diagnostic Report:** Generates a text report containing prediction details and recommendations.
- **Prediction History:** Maintains recent scan information during the application session.

## 🧠 Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Streamlit | Web application development |
| PyTorch | Deep learning framework |
| MobileNetV2 | Pretrained CNN architecture |
| Hugging Face Transformers | Pretrained model integration |
| Pillow (PIL) | Image processing |
| Pandas | Data handling and analytics |

## 🔬 Model Information

**Model:** MobileNetV2 – PlantVillage Disease Classifier

**Model Source:** Hugging Face

[View Pretrained Model](https://huggingface.co/neghani/plantvillage-mobilenetv2)

The application uses a pretrained image classification model trained on the PlantVillage dataset.

- Architecture: MobileNetV2
- Task: Image Classification
- Number of Classes: 38
- Supported Crops: 14
- Approach: Transfer Learning / Pretrained Model Inference

The model analyzes uploaded leaf images and returns class predictions with corresponding confidence scores.

## ⚙️ Application Workflow

1. User opens the CropCare AI application.
2. User uploads a plant leaf image.
3. The image is processed and prepared for model inference.
4. The pretrained MobileNetV2 model analyzes the image.
5. The application displays the top three predicted classes.
6. Disease information and general care recommendations are presented.
7. The user can download a diagnostic report.

## 🏗️ Project Structure

```text
CropCare-AI/
│
├── CropCare_AI/
│   ├── app.py
│   ├── model.py
│   ├── disease_info.py
│   └── requirements.txt
│
├── benchmark_performance.py
├── test_app_flow.py
├── .gitignore
└── README.md
```

## 💻 Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/VaishnaviLalan106/CropCare-AI.git
```

### 2. Navigate to the project directory

```bash
cd CropCare-AI
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

Windows:

```bash
venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r CropCare_AI/requirements.txt
```

### 6. Run the application

```bash
streamlit run CropCare_AI/app.py
```

The application will open in your browser at:

```text
http://localhost:8501
```

## 🎯 Applications

- Early identification of potential plant diseases.
- Supporting agricultural learning and awareness.
- Helping gardening enthusiasts understand common plant diseases.
- Providing preliminary crop care information.
- Demonstrating practical applications of deep learning in agriculture.

## ⚠️ Limitations

- Predictions depend on image quality and the model's training data.
- Performance may vary with real-world field images, lighting conditions, and different leaf backgrounds.
- Confidence scores represent model outputs and do not guarantee diagnostic accuracy.
- The application is an educational prototype and should not replace professional agricultural diagnosis or expert advice.

## 🔮 Future Enhancements

- Support for additional crop varieties and disease categories.
- Improved performance on real-world field images.
- Regional language support.
- Integration with agricultural expert resources.
- Weather-based crop disease risk insights.

## 👩‍💻 Developer

**Vaishnavi Lalan**

Computer Science and Engineering

Maharaja Institute of Technology, Mysore

**Project:** CropCare AI – AI-Powered Plant Disease Identification System

---

⭐ If you find this project interesting, consider giving the repository a star!

**Live Demo:** https://vaishnavilalan106-cropcare-ai-cropcare-aiapp-f6zwyi.streamlit.app/

**GitHub Repository:** https://github.com/VaishnaviLalan106/CropCare-AI
