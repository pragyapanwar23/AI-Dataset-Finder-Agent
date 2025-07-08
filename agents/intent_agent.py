import os
import openai
import spacy
import json
from dotenv import load_dotenv

# Load spaCy model safely
model_name = "en_core_web_sm"
try:
    nlp = spacy.load(model_name)
except OSError:
    import spacy.cli
    spacy.cli.download(model_name)
    nlp = spacy.load(model_name)

# Load OpenAI key
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("❌ OPENAI_API_KEY not found in environment. Please check your .env file.")

client = openai.OpenAI(api_key=api_key)

def extract_intent(prompt):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Extract domain, task, data_type and keywords from user queries. Reply with JSON only."},
                {"role": "user", "content": prompt}
            ]
        )
        content = response.choices[0].message.content
        return json.loads(content)

    except openai.RateLimitError:
        print("⚠️ API quota exceeded. Using fallback intent extraction.")
        spacy_result = fallback_intent_parser(prompt)
        spacy_result["notice"] = "⚠️ OpenAI quota exceeded. Using spaCy fallback."
        return spacy_result

    except openai.AuthenticationError:
        return {
            "domain": None,
            "task": None,
            "data_type": None,
            "keywords": ["authentication error"],
            "notice": "🔐 Invalid OpenAI API key."
        }

    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        spacy_result = fallback_intent_parser(prompt)
        spacy_result["notice"] = f"⚠️ Unexpected error. Using spaCy fallback."
        return spacy_result

def fallback_intent_parser(prompt):
    doc = nlp(prompt.lower())
    keywords = [chunk.text.strip() for chunk in doc.noun_chunks if len(chunk.text.strip()) > 2]
    return {
        "domain": None,
        "task": None,
        "data_type": None,
        "keywords": keywords
    }
