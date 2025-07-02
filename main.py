
from query_parser import generate_search_query
from dataset_finder import search_kaggle_datasets

def handle_query(prompt):
    query = generate_search_query(prompt)
    results = search_kaggle_datasets(query)

    if not results:
        return "❌ No relevant datasets found. Try a simpler or broader query."
    
    # Convert each dataset dictionary to a readable string
    formatted_results = [
        f"📂 **{d['title']}**\n🔗 [Link]({d['url']})\n📝 {d.get('description', 'No description available')}"
        for d in results
    ]
    
    return "\n\n---\n\n".join(formatted_results)

