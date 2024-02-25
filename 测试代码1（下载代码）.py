import streamlit as st

with open("bcm.png","rb")as f:
    a = f.read()

st.download_button(label="下载优秀",data = a,file_name= "adddd.png")
