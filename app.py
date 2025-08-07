import os
import streamlit as st

from agents.report_agent import generate_report
from agents.evaluate_agent import rank_datasets
from utils.kaggle_utils import authenticate_kaggle

# Load Kaggle credentials
os.environ["KAGGLE_USERNAME"] = st.secrets["KAGGLE_USERNAME"]
os.environ["KAGGLE_KEY"] = st.secrets["KAGGLE_KEY"]

api = authenticate_kaggle()

st.title("AI Dataset Finder")
query = st.text_input("Describe the dataset you need:", "")

if query:
    raw_results = api.dataset_list(search=query)

    datasets = [{
        "title": getattr(d, "title", ""),
        "description": getattr(d, "subtitle", ""),
        "url": f"https://www.kaggle.com/datasets/{getattr(d, 'ref', '')}",
        "ref": getattr(d, "ref", "")
    } for d in raw_results]

    ranked = rank_datasets(query, datasets)

    if ranked:
        st.markdown(generate_report(ranked), unsafe_allow_html=True)
    else:
        st.warning("No relevant datasets found.")
