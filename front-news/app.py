from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "1548ee58bb7e41a9a19b1ec409153c66"  # Replace with your actual API key
BASE_URL = "https://newsapi.org/v2/everything"

@app.route("/", methods=["GET", "POST"])
def index():
    query = "technology"  # Default topic
    if request.method == "POST":
        query = request.form.get("category", "technology")  # Get user input

    params = {
        "q": query,
        "apiKey": API_KEY,
        "pageSize": 8,  # Limit to 5 articles
        "sortBy": "publishedAt",
        "language": "en"
    }

    response = requests.get(BASE_URL, params=params)
    news_data = response.json().get("articles", [])  # Get articles

    return render_template("index.html", articles=news_data, category=query)
    
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)  # Change port to 8080

