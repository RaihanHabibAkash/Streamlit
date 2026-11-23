# Task 4: Text Style Explorer
import streamlit as st

txt = st.text_input("Tell Something")

if txt:
    st.divider()
    st.title(txt)
    st.divider()
    st.header(txt)
    st.divider()
    st.subheader(txt)
    st.divider()
    st.text(txt)