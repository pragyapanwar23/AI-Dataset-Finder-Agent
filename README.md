🔍 AI Dataset Finder Agent
An autonomous agent-based web application that helps researchers, data scientists, and AI practitioners quickly discover relevant datasets using natural language queries.
The app currently integrates with the Kaggle API and uses NLP-based semantic ranking to ensure the most contextually relevant results are shown first.

🚀 Features
Natural Language Query Support – Simply describe the dataset you’re looking for.

Semantic Ranking – Uses SentenceTransformers (all-MiniLM-L6-v2) with cosine similarity to rank datasets based on relevance.

Multiple Agents – Modular architecture with dedicated agents for:

Intent Parsing (extracts keywords from the query)

Dataset Search (queries APIs like Kaggle)

Evaluation (computes semantic similarity scores)

Reporting (formats results into a readable report)

API Integration – Currently supports Kaggle API, extensible to UCI or Hugging Face.

User-Friendly UI – Built with Streamlit for an interactive and clean interface.

Secure Credentials – API keys are stored and accessed via st.secrets.

🛠️ Tech Stack
Programming Language: Python

Frontend: Streamlit

Backend: Modular agent-based design

APIs: Kaggle API (UCI planned)

NLP: SentenceTransformers (all-MiniLM-L6-v2)

Vector Similarity: Cosine Similarity

Data Processing: Pandas, NumPy

Environment: .devcontainer, requirements.txt for dependencies

📦 Installation
Clone the repository

bash
Copy
Edit
git clone https://github.com/pragyapanwar23/AI-Dataset-Finder-Agent
cd ai-dataset-finder-agent
Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
Set up Kaggle API credentials
In your .streamlit/secrets.toml file:

toml
Copy
Edit
KAGGLE_USERNAME = "your_kaggle_username"
KAGGLE_KEY = "your_kaggle_key"
Run the app

bash
Copy
Edit
streamlit run app.py
📖 Usage
Open the app in your browser after running it.

Enter a natural language query such as:

nginx
Copy
Edit
breast cancer mammography dataset
View ranked dataset results with relevance scores and links.

🧠 How It Works
User Query → Intent Agent
Extracts keywords and prepares the search query.

Search Agent → Kaggle API
Fetches metadata of datasets matching the query.

Evaluate Agent → SentenceTransformers
Embeds query and dataset metadata, calculates cosine similarity.

Report Agent → Streamlit UI
Displays ranked datasets with descriptions, URLs, and scores.

📌 Example
Query:
breast cancer mammography dataset

Output:

bash
Copy
Edit
## 🔍 Top 5 Datasets Found

1. CBIS-DDSM: Breast Cancer Image Dataset
🔗 https://www.kaggle.com/datasets/awsaf49/cbis-ddsm-breast-cancer-image-dataset
⭐ Relevance Score: 0.89
Breast cancer screening dataset including digitized film mammography.

...
📅 Future Plans
Add multi-source search (UCI ML Repo, Hugging Face Datasets).

Include engagement metrics (likes, downloads) in ranking.

Deploy the app to Streamlit Cloud or Hugging Face Spaces.
