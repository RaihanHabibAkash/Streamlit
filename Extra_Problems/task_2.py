# Task 2: Image Gallery App
import streamlit as st

images = st.file_uploader(
    "Enter your image (max 3)",
    type=['jpg','jpeg','png'],
    accept_multiple_files=True
)

if images :
    if len(images) > 3:
        st.error("Can't upload more than 3 images")
    else :

        if len(images) == 3 :
            st.success("3 images successfully")

        col = st.columns(len(images))
        for i,per_image in enumerate(images) :
            with col[i]:
                st.image(per_image)