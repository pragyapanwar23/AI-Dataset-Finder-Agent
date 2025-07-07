# query_parser.py

import openai
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Initialize OpenAI client
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_search_query(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",  # Or "gpt-4o" if you have access
        messages=[
            {
                "role": "system",
                "content": "Extract dataset search keywords and metadata from user input. Return a plain search query string."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.2,
    )

    content = response.choices[0].message.content.strip()
    return content
