# app.py

# Patch sqlite3 with modern version to satisfy chromadb
import sys
import importlib
import pysqlite3

sys.modules["sqlite3"] = pysqlite3
importlib.reload(pysqlite3)

import streamlit as st
from main import run_dataset_agent

st.title("🔎 AI Dataset Finder")
user_input = st.text_input("Describe the dataset you need:")

if st.button("Search") and user_input:
    with st.spinner("Finding best datasets..."):
        results = run_dataset_agent(user_input)
        st.markdown(results, unsafe_allow_html=True)
