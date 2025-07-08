# app.py

import os
import streamlit as st
from kaggle.api.kaggle_api_extended import KaggleApi

# Load Kaggle credentials from secrets
os.environ["KAGGLE_USERNAME"] = st.secrets["KAGGLE_USERNAME"]
os.environ["KAGGLE_KEY"] = st.secrets["KAGGLE_KEY"]

# Authenticate and search
api = KaggleApi()
api.authenticate()

st.title("🔎 AI Dataset Finder")

query = st.text_input("Describe the dataset you need:", "")

if query:
    datasets = api.dataset_list(search=query)
    if datasets:
        st.success(f"Found {len(datasets)} datasets for '{query}':")
        for d in datasets:
            st.write(f"📦 **{d.title}** — `{d.ref}`")
    else:
        st.warning("No datasets found.")
