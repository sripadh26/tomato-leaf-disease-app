# 🍅 Tomato Leaf Disease Detection App

A deep learning–based Streamlit web app that detects tomato leaf diseases using Convolutional Neural Networks (CNN). Users can upload an image and receive instant predictions with suggested remedies.

## 📌 Overview

- **Dataset**: PlantVillage (10+ tomato disease classes)
- **Accuracy**: ~98% using custom CNN
- **Frameworks**: TensorFlow, Keras, Streamlit
- **Input**: `.jpg`, `.png`, `.jpeg` images
- **Output**: Disease class + remedy info

## 🚀 Features

- Real-time tomato leaf disease prediction
- Clean UI with Streamlit
- Model trained on 18,000+ images
- Easy to run locally or deploy online

## 🧠 Model Summary

- Input shape: (128, 128, 3)
- Layers: Conv2D, MaxPooling2D, Dropout, Dense
- Loss: Categorical Crossentropy | Optimizer: Adam

## 🛠️ How to Run

### 1. Clone this repo
```bash
git clone https://github.com/sripadh26/tomato-leaf-disease-app.git
cd tomato-leaf-disease-app
```

### 2. Install requirements
```bash
pip install -r requirements.txt
```

### 3. Run the app
```bash
streamlit run app.py
```

Then open `http://localhost:8501` in your browser.

## 📦 Project Structure

```
tomato-leaf-disease-app/
├── app.py
├── tomato_leaf_model.h5
├── requirements.txt
├── runtime.txt (optional)
└── README.md
```

## 📄 License

Free to use for educational and non-commercial purposes.

## 🙋 Author

**Sripadh**  
🔗 [GitHub Profile](https://github.com/sripadh26)
