# main.py

from memory.memory_store import check_memory, save_to_memory

def run_dataset_agent(prompt):
    from agents.intent_agent import extract_intent
    from agents.search_agent import search_all_sources
    from agents.evaluate_agent import rank_datasets
    from agents.report_agent import generate_report

    cached = check_memory(prompt)
    if cached:
        return f"⚡️ Using memory (cached)\n\n{cached[0]}"

    intent = extract_intent(prompt)
    
    # ✅ Add this line to inspect what was extracted
    print(f"[Intent] Extracted: {intent}")  # 👈 Add this for debugging

    raw_results = search_all_sources(intent)
    top_datasets = rank_datasets(prompt, raw_results)
    report = generate_report(top_datasets)

    save_to_memory(prompt, report)
    return report
