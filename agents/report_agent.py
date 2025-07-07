# agents/report_agent.py

def generate_report(datasets):
    if not datasets:
        return "**No relevant datasets found. Try different keywords.**"

    report = [f"## 🔍 Top {len(datasets)} Datasets Found\n"]
    for idx, d in enumerate(datasets, 1):
        title = d['title'].strip()
        url = d['url']
        desc = d['description'].strip()
        score = f"{d['score']:.2f}" if "score" in d else "N/A"

        report.append(
            f"""**{idx}. {title}** [🔗](<{url}>) <span style='color:#1f77b4;'>⭐ Relevance Score: {score}</span>\n\n{desc}\n"""
        )

    return "\n".join(report)
