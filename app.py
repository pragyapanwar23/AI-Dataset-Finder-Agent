# app.py

import os
import sys
import streamlit as st
from kaggle.api.kaggle_api_extended import KaggleApi

# Use current working directory instead of __file__ for cloud compatibility
sys.path.append(os.getcwd())

from agents.report_agent import generate_report
from agents.evaluate_agent import rank_datasets
from utils.kaggle_utils import authenticate_kaggle

# Load Kaggle credentials from Streamlit secrets
os.environ["KAGGLE_USERNAME"] = st.secrets["KAGGLE_USERNAME"]
os.environ["KAGGLE_KEY"] = st.secrets["KAGGLE_KEY"]

# Authenticate Kaggle API
api = authenticate_kaggle()

# Streamlit UI
st.title("🔎 AI Dataset Finder")

query = st.text_input("Describe the dataset you need:", "")

if query:
    # Search datasets
    raw_results = api.dataset_list(search=query)

    # Convert to plain dict
    datasets = []
    for d in raw_results:
        datasets.append({
            "title": getattr(d, "title", ""),
            "description": getattr(d, "subtitle", ""),
            "url": f"https://www.kaggle.com/datasets/{getattr(d, 'ref', '')}",
            "ref": getattr(d, "ref", "")
        })

    # Rank and display
    ranked = rank_datasets(query, datasets)

    if ranked:
        st.markdown(generate_report(ranked), unsafe_allow_html=True)
    else:
        st.warning("No relevant datasets found.")
