from sentence_transformers import SentenceTransformer, util

GENERIC_TITLES = {
    "datasets", "view datasets", "browse datasets", 
    "contribute dataset", "donate a dataset"
}

def is_generic_title(title):
    return "dataset" in title.lower() and title.strip().lower() in GENERIC_TITLES

def rank_datasets(prompt, datasets):
    model = SentenceTransformer("all-MiniLM-L6-v2")
    query_embedding = model.encode(prompt, convert_to_tensor=True)

    ranked = []
    for d in datasets:
        title = d.get("title", "").strip()
        desc = d.get("description", "").strip()
        text = f"{title}. {desc}".strip()

        if not text or len(desc) < 10:
            continue

        if is_generic_title(title):
            continue  # always skip these

        # Score based on similarity
        d["score"] = util.cos_sim(query_embedding, model.encode(text, convert_to_tensor=True))[0][0].item()
        ranked.append(d)

    # Sort and return best matches
    ranked = sorted(ranked, key=lambda x: x["score"], reverse=True)
    return [d for d in ranked if d["score"] >= 0.4][:20]
