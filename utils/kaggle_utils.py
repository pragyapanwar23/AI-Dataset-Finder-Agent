# utils/kaggle_utils.py

import os
from kaggle.api.kaggle_api_extended import KaggleApi

def authenticate_kaggle():
    # Try setting from Streamlit secrets if not already set
    if "KAGGLE_USERNAME" not in os.environ or "KAGGLE_KEY" not in os.environ:
        try:
            import streamlit as st
            os.environ["KAGGLE_USERNAME"] = st.secrets["KAGGLE_USERNAME"]
            os.environ["KAGGLE_KEY"] = st.secrets["KAGGLE_KEY"]
        except Exception as e:
            raise RuntimeError("❌ Kaggle credentials missing and Streamlit secrets unavailable.") from e

    api = KaggleApi()
    api.authenticate()
    return api

def search_kaggle(intent_dict, max_results=20):
    query = intent_dict.get("keywords", "")
    if isinstance(query, list):
        query = " ".join(query)
    elif not isinstance(query, str):
        query = str(query)

    api = authenticate_kaggle()

    kaggle_results = api.dataset_list(search=query)

    datasets = []
    for r in kaggle_results[:max_results]:
        datasets.append({
            "title": getattr(r, "title", ""),
            "description": getattr(r, "subtitle", ""),
            "url": f"https://www.kaggle.com/datasets/{getattr(r, 'ref', '')}",
            "ref": getattr(r, "ref", "")
        })

    return datasets
