import streamlit as st
from PIL import Image
from model.predict import generate_caption

st.set_page_config(page_title="Image Caption Generator", layout="wide")

st.title("🖼️ AI Image Caption Generator")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    if st.button("Generate Caption"):
        caption = generate_caption(image)
        st.subheader("🧠 Generated Caption")
        st.write(caption)
