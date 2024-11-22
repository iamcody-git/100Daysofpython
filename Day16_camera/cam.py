import streamlit as st # type: ignore
from PIL import Image # type: ignore

camera_image = st.camera_input("camera")
print(camera_image)

if camera_image:
    img = Image.open(camera_image)
    grey_img = img.convert("L")
    st.image(grey_img)
