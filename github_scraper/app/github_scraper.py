import time

import requests

from app.access_token import PERSONAL_ACCESS_TOKEN

from .models import UserInfo

TOKEN = PERSONAL_ACCESS_TOKEN

autorization = {"Autorization": f"token {TOKEN}"}


def get_users(per_page=100, max_users=500):
    users = []
    since_id = 1

    while len(users) < max_users:
        url = "https://api.github.com/users"
        since_per_page = {"since": since_id, "per_page": per_page}

        response = requests.get(url, headers=autorization, params=since_per_page)

        if response.status_code != 200:
            print("Error:", response.json())
            break

        batch_users = response.json()
        users.extend(batch_users)
        save_to_database(batch_users)
        since_id = batch_users[-1]["id"]
        time.sleep(0.200)

    print(f"Users fetched: {len(users)}")


def save_to_database(users):
    for user in users:
        print(user)
        UserInfo.objects.update_or_create(
            id=user["id"],
            defaults={
                "login": user["login"],
                "html_url": user["html_url"],
                "repos_url": user.get("repos_url", "N/A"),
                "user_type": user.get("type", "Unknown"),
            },
        )
