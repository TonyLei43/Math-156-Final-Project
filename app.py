import streamlit as st
import numpy as np
from PIL import Image
import tensorflow as tf
from tensorflow.keras.preprocessing import image

#load model
@st.cache_resource
def load_model():
    model = tf.keras.models.load_model('model_1.h5')
    return model

model = load_model()

#preprocess image
def preprocess_image(uploaded_image, target_size=(224, 224)):
    img = uploaded_image.resize(target_size)
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0) 
    img_array /= 255.0  
    return img_array

#predict image
def predict(model, img_array):
    prediction = model.predict(img_array)
    return 'Royce Hall' if prediction[0][0] > 0.5 else 'Not Royce Hall'


def main():
    st.title("Is It Royce Hall?")

    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image.', use_column_width=True)
        st.write("")
        st.write("Classifying...")

        img_array = preprocess_image(image)
        prediction = predict(model, img_array)

        st.write(f'Predicted class: {prediction}')

if __name__ == "__main__":
    main()
