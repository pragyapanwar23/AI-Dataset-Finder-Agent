import os
import streamlit as st
from kaggle.api.kaggle_api_extended import KaggleApi
from agents.report_agent import generate_report

# Load Kaggle credentials from secrets
os.environ["KAGGLE_USERNAME"] = st.secrets["KAGGLE_USERNAME"]
os.environ["KAGGLE_KEY"] = st.secrets["KAGGLE_KEY"]

# Authenticate and search
api = KaggleApi()
api.authenticate()

st.title("🔎 AI Dataset Finder")

query = st.text_input("Describe the dataset you need:", "")

if query:
    kaggle_results = api.dataset_list(search=query)

    if kaggle_results:
        datasets = []
        for d in kaggle_results:
            datasets.append({
                "title": d.title,
                "description": d.subtitle or "No description provided.",
                "url": f"https://www.kaggle.com/datasets/{d.ref}",
                "score": 1.0  # Optional: dummy or real value
            })

        st.markdown(generate_report(datasets))
    else:
        st.warning("No datasets found.")
