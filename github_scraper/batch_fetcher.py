import json

import requests

url_users = "https://api.github.com/users"

response = requests.get(url_users)

users_info = response.json()

print(f"{len(users_info)}")

with open("github_users.json", "w") as file:
    json.dump(users_info, file, indent=1)
