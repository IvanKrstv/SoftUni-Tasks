import requests

print("How many astronauts are there in the space right now?\n")
counter = 0

# Getting the response
response = requests.get("http://api.open-notify.org/astros.json")

# Checking if we got the data
if response.status_code != 200:
    print("There was an error fetching data.")
else:
    # Converting the response into dictionary
    dic = response.json()

    for person in dic['people']:
        print(person['name'])

    print(f"\nTotal astronauts: {dic['number']}")

