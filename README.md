# 🌿 AI Plant Disease Detector
### Deep Learning | CNN | Image Classification | Flask Web App

This project is an end-to-end **AI-based Plant Disease Detection system** that identifies diseases from leaf images.  
It uses a **Convolutional Neural Network (CNN)** trained on a dataset of **23 plant disease classes** and provides predictions through an interactive **Flask web interface**.

---

## 🚀 Features

✔ Detect plant diseases from uploaded leaf images  
✔ Classifies into **23 plant species & diseases**  
✔ CNN built using **TensorFlow / Keras**  
✔ Confidence percentage for each prediction  
✔ Shows “Low Confidence Warning” for unclear images  
✔ Full web interface using **Flask + HTML/CSS + JS**  
✔ Supports mobile camera image upload  
✔ Easy to deploy on **Railway / Render / VPS**

---

## 🧠 Model Details

- **Model Type:** Convolutional Neural Network (CNN)  
- **Input Size:** 160x160 RGB images  
- **Activation:** ReLU + Softmax  
- **Loss:** Categorical Crossentropy  
- **Optimizer:** Adam  
- **Accuracy Achieved:** ~90% (test accuracy  
- **Dataset:** Plant Disease dataset (23 classes)

---
plant-disease-app/
│── app.py
│── requirements.txt
│── Procfile
│── model/
│ └── plant_disease_cnn_model.h5
│── static/
│ └── uploads/
│── templates/
│ └── index.html
│── README.md


---

## 🖼️ Web Interface Preview

- Upload plant leaf image  
- App predicts disease + confidence score  
- Shows warnings when confidence < 50%  
- Clean modern UI  

---

## 🔧 Installation & Setup (Local)

### 1️⃣ Clone repo
git clone https://github.com/YOUR_USERNAME/plant-disease-detector.git

cd plant-disease-detector

---

## 📌 Classes Detected

- Apple: Apple_scab, Black_rot, Cedar_rust, healthy  
- Corn: Leaf spot, Rust, Blight, healthy  
- Pepper: Bacterial spot, healthy  
- Potato: Early blight, Late blight, healthy  
- Tomato: 11 different diseases + healthy  

Total Classes: **23**

---

## 🎯 Future Improvements

- Add Grad-CAM heatmaps  
- Add multiple model versions (EfficientNetB0, MobileNetV2)  
- Add real-time camera classification  
- Build mobile app version  
- Add dataset cleaning/augmentation scripts  

---

## 🙋‍♂️ Author

**Nilesh Jadhav**  
AI/ML Engineer | Deep Learning | Computer Vision  
📧 Contact: nileshjadhav4145@gmail.com

---

## ⭐ Support

If you like this project, consider giving it a ⭐ on GitHub!  


