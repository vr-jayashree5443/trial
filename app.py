import streamlit as st
from PIL import Image

st.title("Attempt5")
st.header("Header")
file=st.file_uploader("Uploadfile")
#image=Image.open(file)
#st.image(image)
#st.write(image)

st.selectbox("navigation",("Demo1","Demo2"))