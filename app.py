import streamlit as st
from main import handle_query  # This will do nothing for now

st.set_page_config(page_title="AI Dataset Finder", layout="centered")

st.title("🔍 AI Dataset Finder")
st.markdown("Describe your research or project goal, and I'll help you find relevant datasets!")

# Text input from user
user_input = st.text_area("What kind of dataset are you looking for?", height=150)

# Button to trigger the search
if st.button("Search for Datasets"):
    if not user_input.strip():
        st.warning("Please enter a description of your dataset needs.")
    else:
        st.info("🔄 Searching for relevant datasets...")
        result = handle_query(user_input)
        st.success("✅ Done! (placeholder)")
        st.markdown(result)

import streamlit as st
from main import handle_query  # This will do nothing for now

st.set_page_config(page_title="AI Dataset Finder", layout="centered")

st.title("🔍 AI Dataset Finder")
st.markdown("Describe your research or project goal, and I'll help you find relevant datasets!")

# Text input from user
user_input = st.text_area("What kind of dataset are you looking for?", height=150)

# Button to trigger the search
if st.button("Search for Datasets"):
    if not user_input.strip():
        st.warning("Please enter a description of your dataset needs.")
    else:
        st.info("🔄 Searching for relevant datasets...")
        result = handle_query(user_input)
        st.success("✅ Done! (placeholder)")
        st.markdown(result)
