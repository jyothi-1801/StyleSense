import streamlit as st
import numpy as np
from PIL import Image

st.title("👗 StyleAI - AI Fashion Advisor")

st.write("Upload your photo and get fashion recommendations.")

uploaded_file = st.file_uploader("Upload Image", type=["jpg","png","jpeg"])

gender = st.selectbox("Select Gender", ["Male","Female"])


def detect_skin_tone(image):

    img = np.array(image)

    avg_color = img.mean(axis=0).mean(axis=0)

    r,g,b = avg_color

    if r > 180:
        return "Fair"
    elif r > 140:
        return "Medium"
    elif r > 100:
        return "Olive"
    else:
        return "Deep"


def get_style(skin_tone):

    if skin_tone == "Fair":
        return "Try Navy Blue, Burgundy and Dark Green outfits."

    elif skin_tone == "Medium":
        return "Earth tones like Olive, Brown and Mustard will suit you."

    elif skin_tone == "Olive":
        return "Try Cream, Rust and Teal outfits."

    else:
        return "Bright colors like White, Yellow and Red will suit you."


if uploaded_file is not None:

    image = Image.open(uploaded_file)

    st.image(image, caption="Uploaded Image", use_container_width=True)

    if st.button("Analyze Style"):

        skin_tone = detect_skin_tone(image)

        recommendation = get_style(skin_tone)

        st.subheader("Detected Skin Tone")
        st.success(skin_tone)

        st.subheader("Style Recommendation")
        st.write(recommendation)