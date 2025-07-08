# utils/kaggle_utils.py

import os
from kaggle.api.kaggle_api_extended import KaggleApi

def search_kaggle(intent_dict, max_results=20):
    keywords = intent_dict.get("keywords", [])
    if isinstance(keywords, str):
        keywords = [keywords]
    query = " ".join(keywords)

    api = KaggleApi()
    api.authenticate()

    kaggle_results = api.dataset_list(search=query)

    datasets = []
    for r in kaggle_results[:max_results]:
        title = getattr(r, "title", "")
        subtitle = getattr(r, "subtitle", "")
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
