# query_parser.py

import spacy

nlp = spacy.load("en_core_web_sm")

def extract_keywords(prompt):
    doc = nlp(prompt.lower())
    keywords = [chunk.text.strip() for chunk in doc.noun_chunks if len(chunk.text.strip()) > 2]
    return keywords

def build_search_query(keywords):
    return " ".join(keywords)

def generate_search_query(prompt):  # <- This function MUST be present!
    keywords = extract_keywords(prompt)
    return build_search_query(keywords)
