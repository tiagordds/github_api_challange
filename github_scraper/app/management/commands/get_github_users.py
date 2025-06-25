import time

import requests
from django.core.management.base import BaseCommand

from app.access_token import PERSONAL_ACCESS_TOKEN
from app.models import UserInfo

TOKEN = PERSONAL_ACCESS_TOKEN
authorization = {"Authorization": f"token {TOKEN}"}


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("--since_id", type=int, default=0)
        parser.add_argument("--per_page", type=int, default=100)
        parser.add_argument("--max_users", type=int, default=500)

    def handle(self, *args, **options):
        since_id = options["since_id"]
        per_page = options["per_page"]
        max_users = options["max_users"]
        self.get_users(since_id, per_page, max_users)

    def get_users(self, since_id=0, per_page=100, max_users=500):
        users = []

        while len(users) < max_users:
            url = "https://api.github.com/users"
            since_per_page = {"since": since_id, "per_page": per_page}

            response = requests.get(url, headers=authorization, params=since_per_page)

            if response.status_code != 200:
                break

            batch_users = response.json()
            users.extend(batch_users)
            self.save_to_database(batch_users)
            since_id = batch_users[-1]["id"]
            time.sleep(0.200)

    def save_to_database(self, users):
        for user in users:
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
