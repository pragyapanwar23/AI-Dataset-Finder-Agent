

import boot  # <-- Must be before ANYTHING else
import os
import streamlit as st
from main import run_dataset_agent
from kaggle.api.kaggle_api_extended import KaggleApi

# Load Kaggle credentials from secrets
os.environ["KAGGLE_USERNAME"] = st.secrets["KAGGLE_USERNAME"]
os.environ["KAGGLE_KEY"] = st.secrets["KAGGLE_KEY"]

# Authenticate and search
api = KaggleApi()
api.authenticate()

st.title("🔎 AI Dataset Finder")
user_input = st.text_input("Describe the dataset you need:")

if st.button("Search") and user_input:
    with st.spinner("Finding best datasets..."):
        results = run_dataset_agent(user_input)
        st.markdown(results, unsafe_allow_html=True)
query = st.text_input("Describe the dataset you need:", "")

if query:
    datasets = api.dataset_list(search=query)
    if datasets:
        st.success(f"Found {len(datasets)} datasets for '{query}':")
        for d in datasets:
            st.write(f"📦 **{d.title}** — `{d.ref}`")
    else:
        st.warning("No datasets found.")
