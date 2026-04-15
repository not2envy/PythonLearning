import requests

#filtering API data
response = requests.get("https://jsonplaceholder.typicode.com/users")

data = response.json()
users = data

filtered = [user["name"] for user in users if user["id"] > 5]

print(filtered)