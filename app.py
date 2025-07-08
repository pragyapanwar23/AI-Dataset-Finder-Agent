# app.py

import streamlit as st
from main import run_dataset_agent

st.title("🔎 AI Dataset Finder")
st.write("Describe the dataset you need:")

user_input = st.text_input("What kind of dataset are you looking for?", "")

if st.button("Search"):
    if not user_input.strip():
        st.warning("Please enter a query.")
    else:
        with st.spinner("Searching datasets..."):
            results = run_dataset_agent(user_input)
            st.markdown(results, unsafe_allow_html=True)
