import streamlit as st

with open('LabManual.md') as file:

    st.markdown(file.read())