import requests

def get_market_news(sector):

    url = f"https://api.duckduckgo.com/?q={sector}+india+market+news&format=json"

    res = requests.get(url)

    data = res.json()

    results = []

    for topic in data.get("RelatedTopics", [])[:5]:
        if "Text" in topic:
            results.append(topic["Text"])

    return results