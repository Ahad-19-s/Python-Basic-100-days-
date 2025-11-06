import requests
import argparse
import json
import os
import time

# -----------------------------
# CLI Setup
# -----------------------------
parser = argparse.ArgumentParser(description="Fetch news by topic using NewsAPI")
parser.add_argument(
    "-t", "--topic",
    type=str,
    required=True,
    help="Topic to fetch news about"
)
parser.add_argument(
    "-n", "--number",
    type=int,
    default=5,
    help="Number of news articles to display (default: 5)"
)
args = parser.parse_args()

# -----------------------------
# NewsAPI Configuration
# -----------------------------
API_KEY = "cfaf381788814bca9d94c9b02674a274"  # Replace with your NewsAPI key
BASE_URL = "https://newsapi.org/v2/everything"

# -----------------------------
# Fetch news from NewsAPI
# -----------------------------
params = {
    "q": args.topic,            # Search query / topic
    "pageSize": args.number,    # Number of articles to fetch
    "sortBy": "publishedAt",    # Sort by latest
    "language": "en",
    "apiKey": API_KEY
}

try:
    response = requests.get(BASE_URL, params=params, timeout=5)
    response.raise_for_status()       # Raise HTTPError if status != 200
    news_data = response.json()       # Convert response to Python dict
except requests.exceptions.RequestException as e:
    print("Error fetching news:", e)
    exit(1)

# -----------------------------
# Display news in terminal
# -----------------------------
articles = news_data.get("articles", [])

if not articles:
    print(f"No news found for topic: {args.topic}")
else:
    print(f"\nTop {len(articles)} news articles about '{args.topic}':\n")
    for i, article in enumerate(articles, 1):
        title = article.get('title', 'No title')
        source = article.get('source', {}).get('name', 'Unknown')
        published_at = article.get('publishedAt', 'Unknown')
        url = article.get('url', 'No URL')

        print(f"{i}. {title}")
        print(f"   Source      : {source}")
        print(f"   Published At: {published_at}")
        print(f"   URL         : {url}\n")

# -----------------------------
# Save news to JSON file (with timestamp)
# -----------------------------
os.makedirs("news_backup", exist_ok=True)
timestamp = time.strftime("%Y%m%d_%H%M%S")
filename = os.path.join("news_backup", f"{args.topic}_news_{timestamp}.json")

with open(filename, "w", encoding="utf-8") as f:
    json.dump(articles, f, indent=2)

print(f"News saved to {filename}")

