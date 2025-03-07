
# import requests
# from bs4 import BeautifulSoup  

# x = requests.get('https://scpoolsinc.com/')

# soup = BeautifulSoup(x.text, "html.parser")
# for heading in soup.find_all("h2"):
#     print(heading.text)

# print(x.text)

import requests
import json  # Import json module for formatting

# Search GitHub's repositories for popular PHP projects
response = requests.get(
    "https://api.github.com/search/repositories",
    params={"q": "language:php", "sort": "stars", "order": "desc"},
)

# Check if the request was successful
if response.status_code == 200:
    json_response = response.json()
    
    print("helllllllllll")
    
    # Pretty-print the JSON response
    print(json.dumps(json_response, indent=4))
    
    # Extract popular repositories
    popular_repositories = json_response.get("items", [])
    
    # Print details of the first three repositories
    for repo in popular_repositories[:3]:
        print(f"Name: {repo['name']}")
        print(f"Description: {repo['description']}")
        print(f"Stars: {repo['stargazers_count']}")
        print()
else:
    print(f"GitHub API request failed with status code {response.status_code}")
