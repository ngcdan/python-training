import requests

people = requests.get("http://api.open-notify.org/astros.json")
json = people.json()

print(json)
