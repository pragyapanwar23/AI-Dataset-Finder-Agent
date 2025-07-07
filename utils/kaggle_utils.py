# utils/kaggle_utils.py

from kaggle.api.kaggle_api_extended import KaggleApi

def search_kaggle(intent_dict, max_results=20):
    query = intent_dict.get("keywords", "")
    if isinstance(query, list):
        query = " ".join(query)
    elif not isinstance(query, str):
        query = str(query)

    api = KaggleApi()
    api.authenticate()

    kaggle_results = api.dataset_list(search=query)

    # Convert each ApiDataset object to a dictionary
    datasets = []
    for r in kaggle_results[:max_results]:
        datasets.append({
            "title": getattr(r, "title", ""),
            "description": getattr(r, "subtitle", ""),  # Kaggle uses `subtitle` for short description
            "url": f"https://www.kaggle.com/datasets/{getattr(r, 'ref', '')}",
            "ref": getattr(r, "ref", "")
        })

    return datasets
