import streamlit as st

# st.write("Hello World")

st.title(":world_map: Raihan Habib Akash", anchor=False)

st.header("Header 1", divider=True)
st.subheader("SubHeader 2")
st.text("Bro Code")

st.markdown(":red[**Hello**] *world*")
st.markdown(":green-background[:yellow[**Hello**] *world*]")

a = 10 ; b = 20
st.write(a+b)