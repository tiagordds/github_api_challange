import time

import requests

from app.access_token import PERSONAL_ACCESS_TOKEN

from .models import UserInfo

TOKEN = PERSONAL_ACCESS_TOKEN

autorization = {"Autorization": f"token {TOKEN}"}


def get_users(since_id=0, per_page=100, max_users=500):
    users = []
    since_id = 10000

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
        # print(user)
        UserInfo.objects.update_or_create(
            id=user.get("id"),
            defaults={
                "login": user.get("login"),
                "avatar_url": user.get("avatar_url", "Unknown"),
                "html_url": user.get("html_url", "Unknown"),
                "followers_url": user.get("followers_url", "Unknown"),
                "following_url": user.get("following_url", "Unknown"),
                "gist_url": user.get("gist_url", "Unknown"),
                "starred_url": user.get("starred_url", "Unknown"),
                "subscriptions_url": user.get("subscriptions_url", "Unknown"),
                "organizations_url": user.get("organizations_url", "Unknown"),
                "repos_url": user.get("repos_url", "Unknown"),
                "event_url": user.get("event_url", "Unknown"),
                "received_events_url": user.get("received_events_url", "Unknown"),
                "user_type": user.get("user_type", "Unknown"),
                "user_view_type": user.get("user_view_type", "Unknown"),
                "site_admin": user.get("site_admin", False),
            },
        )
