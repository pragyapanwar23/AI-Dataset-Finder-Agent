import streamlit as st
from agents.intent_agent import extract_intent
from agents.search_agent import search_all_sources
from agents.report_agent import generate_report

st.set_page_config(page_title="🔎 AI Dataset Finder")

st.title("🔎 AI Dataset Finder")
st.markdown("Describe the dataset you need:")

user_input = st.text_input("")

if user_input:
    with st.spinner("Analyzing your request..."):
        intent = extract_intent(user_input)
        results = search_all_sources(intent)
        report = generate_report(results)
        st.markdown(report, unsafe_allow_html=True)
