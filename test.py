import requests


API_KEY = "b7a5e5365379415fb44da1db110c1d02"
url = f"https://newsapi.org/v2/everything?q=bitcoin&apiKey={API_KEY}"
response = requests.get(url)
data = response.json()
print(data)