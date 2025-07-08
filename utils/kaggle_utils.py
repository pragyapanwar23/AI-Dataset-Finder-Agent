# utils/kaggle_utils.py

import os
import re
from kaggle.api.kaggle_api_extended import KaggleApi

def authenticate_kaggle():
    if "KAGGLE_USERNAME" not in os.environ or "KAGGLE_KEY" not in os.environ:
        try:
            import streamlit as st
            os.environ["KAGGLE_USERNAME"] = st.secrets["KAGGLE_USERNAME"]
            os.environ["KAGGLE_KEY"] = st.secrets["KAGGLE_KEY"]
        except Exception as e:
            raise RuntimeError("❌ Kaggle credentials missing and Streamlit secrets unavailable.") from e
def search_kaggle(intent_dict, max_results=20):
    keywords = intent_dict.get("keywords", [])
    if isinstance(keywords, str):
        keywords = [keywords]
    query = " ".join(keywords)

    api = KaggleApi()
    api.authenticate()
    return api

def keyword_match_score(text, keywords):
    if not text or not keywords:
        return 0
    text = text.lower()
    score = sum(1 for kw in keywords if kw.lower() in text)
    return score / len(keywords)

def search_kaggle(intent_dict, max_results=20):
    query_keywords = intent_dict.get("keywords", [])
    query = " ".join(query_keywords) if isinstance(query_keywords, list) else str(query_keywords)

    api = authenticate_kaggle()
    kaggle_results = api.dataset_list(search=query)

    datasets = []
    for r in kaggle_results[:max_results]:
        title = getattr(r, "title", "")
        subtitle = getattr(r, "subtitle", "")
        combined_text = f"{title} {subtitle}"
        score = keyword_match_score(combined_text, query_keywords)
        full_text = f"{title} {subtitle}".lower()

        # Simple keyword match score
        match_count = sum(1 for kw in keywords if kw.lower() in full_text)
        score = match_count / len(keywords) if keywords else 0

        datasets.append({
            "title": title,
            "description": subtitle,
            "url": f"https://www.kaggle.com/datasets/{getattr(r, 'ref', '')}",
            "ref": getattr(r, "ref", ""),
            "score": score
        })

    # Sort by score descending
    datasets.sort(key=lambda x: x["score"], reverse=True)
    return datasets
