import json
import time

import requests
from access_token import PERSONAL_ACCESS_TOKEN

TOKEN = PERSONAL_ACCESS_TOKEN

autorization = {"Autorization": f"token {TOKEN}"}


def get_users(per_page=100, max_users=1000):
    users = []
    since_id = 0

    while len(users) < max_users:
        url = "https://api.github.com/users"
        since_per_page = {"since": since_id, "per_page": per_page}

        response = requests.get(url, headers=autorization, params=since_per_page)

        if response.status_code == 200:
            batch_users = response.json()

        users.extend(batch_users)
        since_id = batch_users[-1]["id"]

        time.sleep(0.200)

        with open("github_users.json", "w") as file:
            json.dump(users, file, indent=1)
    print(len(users))


get_users()
