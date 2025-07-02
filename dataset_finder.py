
from kaggle.api.kaggle_api_extended import KaggleApi
from query_parser import generate_search_query as generate_query



def search_kaggle_datasets(user_prompt, max_results=5):
    api = KaggleApi()
    api.authenticate()

    query = generate_query(user_prompt)
    results = api.dataset_list(search=query)[:max_results]

    datasets = []
    for dataset in results:
        datasets.append({
    "title": dataset.title,
    "ref": dataset.ref,
    "url": f"https://www.kaggle.com/datasets/{dataset.ref}",
    "description": dataset.subtitle
    # "size": dataset.totalBytes  # Optional: uncomment if you want size in bytes
 })
    return datasets
