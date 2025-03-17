import requests

# URL of the API
url = "https://webhook.site/2be3f7dd-99a2-4b55-900b-526053818ea9"


new_data = {
    'userId': 2,
    'id': 1,
    'title': "Random txt"
}

response = requests.put(url, new_data)

# Convert the response to json
data = response.json()

print(response.status_code)
print(data)