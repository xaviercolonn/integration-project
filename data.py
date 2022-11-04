import requests

# Get the data
result = requests.get("https://opentdb.com/api.php?amount=10&category=17&type=boolean")
result = result.json()
q_data = result["results"]
