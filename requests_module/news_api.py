import requests
import json

API_KEY = "1548ee58bb7e41a9a19b1ec409153c66"  # Replace with your actual API key
BASE_URL = "https://newsapi.org/v2/top-headlines"

# Ask the user for a topic to search
user_query = input("Enter a topic (e.g., sports, market, technology, health): ").strip()

# Define query parameters
params = {
    "q": user_query,  # Search for the user's topic
    "apiKey": API_KEY,
    "pageSize": 5,  # Limit the results to 5 articles
    "sortBy": "publishedAt",  # Sort results by latest published articles
    "language": "en"  # Fetch English news
}

# Make the API request
response = requests.get(BASE_URL, params=params)

# Check if the request was successful
if response.status_code == 200:
    json_response = response.json()
    
    # Check if articles are found
    articles = json_response.get("articles", [])
    if articles:
        print("\nTop News Articles:\n")
        for index, article in enumerate(articles, start=1):
            print(f"{index}. Title: {article['title']}")
            print(f"   Source: {article['source']['name']}")
            print(f"   Published At: {article['publishedAt']}")
            print(f"   URL: {article['url']}\n")
    else:
        print("No news articles found for this topic.")
else:
    print(f"Error: {response.status_code}, {response.text}")  # Print error message if request fails
