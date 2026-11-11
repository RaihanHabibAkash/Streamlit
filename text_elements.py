import streamlit as st 

# anchor=False -> Side ar default link ar option ta shorai
st.title(":world_map: My first Streamlit Web Apps",anchor=False)

# divider -> thin akta line
st.header("Content 1",divider=True)
st.subheader("Content 1 Subheader")



st.text("Hello world")



st.markdown(":red[**Hello**] *world* ")

st.markdown(":red-background[:orange[**Hello**] *world*] :world_map:")

a = 10 
b= 20 

st.write(a,b)