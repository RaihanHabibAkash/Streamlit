# Task 1: Personal Info Card App

import streamlit as st

text = st.text_input("Enter the text here")
num = st.number_input("Enter the number here", value=None)
pesha = st.selectbox(
    "Chose profession",
    ("Student", "Employee", "Businessman", "Freelancer"),
    index=None
)

pressed = st.button("Enter to Confirm", type="primary")

if pressed :
    if text and num and pesha :
        st.success(f"Your test is {text}\n")
        st.success(f"Your number is {num}\n")
        st.success(f"Your Profession is {pesha}\n")
    else :
        st.warning("Enter all the fields")
