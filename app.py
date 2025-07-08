# app.py

import boot  # <-- Must be before ANYTHING else
import streamlit as st
from main import run_dataset_agent

st.title("🔎 AI Dataset Finder")
user_input = st.text_input("Describe the dataset you need:")

if st.button("Search") and user_input:
    with st.spinner("Finding best datasets..."):
        results = run_dataset_agent(user_input)
        st.markdown(results, unsafe_allow_html=True)
