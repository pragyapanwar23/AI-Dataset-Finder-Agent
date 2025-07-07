from utils.kaggle_utils import search_kaggle
from utils.uci_scraper import search_uci

def search_all_sources(intent_dict):
    kaggle = search_kaggle(intent_dict, max_results=20)  # grab more
    uci = search_uci(intent_dict)
    return kaggle + uci  # do not slice here — let ranker cut to 10


