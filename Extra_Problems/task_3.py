# Task 3: Audio & Video Player App

import streamlit as st

audio_file = st.file_uploader(
    "Enter audio",
    type=['mp3', 'ogg']
)
video_file = st.file_uploader(
    "Enter Video",
    type=['mp4','mkv']
)

pressed = st.button("Enter",type="primary")


if pressed :
    if video_file and audio_file :
        st.video(video_file)
        st.audio(audio_file)
    else :
        st.error("you must upload the files")