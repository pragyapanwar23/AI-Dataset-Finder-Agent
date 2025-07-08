# app.py

import os
import sys

# Add the current directory to Python path to allow relative imports
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import streamlit as st
from kaggle.api.kaggle_api_extended import KaggleApi

from agents.report_agent import generate_report
from utils.kaggle_utils import authenticate_kaggle
from agents.evaluate_agent import rank_datasets

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

    # Convert Kaggle dataset metadata to dicts
    datasets = []
    for d in raw_results:
        datasets.append({
            "title": getattr(d, "title", ""),
            "description": getattr(d, "subtitle", ""),
            "url": f"https://www.kaggle.com/datasets/{getattr(d, 'ref', '')}",
            "ref": getattr(d, "ref", "")
        })

    # Rank using sentence-transformers
    ranked = rank_datasets(query, datasets)

    # Display results
    if ranked:
        st.markdown(generate_report(ranked), unsafe_allow_html=True)
    else:
        st.warning("No relevant datasets found.")
