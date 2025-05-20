
import streamlit as st
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np
import os

# Load model
model = load_model("tomato_leaf_model.h5")

class_names = [
    "Tomato___Bacterial_spot",
    "Tomato___Early_blight",
    "Tomato___Late_blight",
    "Tomato___Leaf_Mold",
    "Tomato___Septoria_leaf_spot",
    "Tomato___Spider_mites_Two_spotted_spider_mite",
    "Tomato___Target_Spot",
    "Tomato___Tomato_Yellow_Leaf_Curl_Virus",
    "Tomato___Tomato_mosaic_virus",
    "Tomato___healthy"
]


# Function to preprocess image
def preprocess_image(image):
    image = image.resize((128, 128))
    image = np.array(image) / 255.0
    image = np.expand_dims(image, axis=0)
    return image

# Title
st.title("🍅 Tomato Leaf Disease Detection App")
st.markdown("Upload a tomato leaf image and get instant diagnosis with remedies.")

# File uploader
uploaded_file = st.file_uploader("Choose a tomato leaf image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    if st.button("Predict"):
        processed_image = preprocess_image(image)
        prediction = model.predict(processed_image)
        predicted_class = class_names[np.argmax(prediction)]

        st.success(f"✅ Predicted Disease: **{predicted_class}**")

        remedies = {
            "Tomato___Early_blight": "Use fungicides with chlorothalonil or copper.",
            "Tomato___Late_blight": "Remove affected plants, use copper-based fungicide.",
            "Tomato___Leaf_Mold": "Ensure air circulation, avoid overhead watering.",
            "Tomato___healthy": "No disease detected, plant is healthy. 🎉"
        }

        if predicted_class in remedies:
            st.info(f"💡 Remedy: {remedies[predicted_class]}")
