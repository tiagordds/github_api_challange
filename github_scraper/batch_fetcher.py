import json
import sqlite3
import time

import requests
from access_token import PERSONAL_ACCESS_TOKEN

TOKEN = PERSONAL_ACCESS_TOKEN

autorization = {"Autorization": f"token {TOKEN}"}


def make_database():
    connection = sqlite3.connect("github_users.db")
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            login TEXT UNIQUE,
            html_url TEXT,
            repos_url TEXT,
            type TEXT
        )
    """)
    connection.commit()
    connection.close()


def save_database(users):
    connection = sqlite3.connect("github_users.db")
    cursor = connection.cursor()
    for user in users:
        cursor.execute(
            """
            INSERT INTO users(id, login, html_url, repos_url, type)
            VALUES (?, ?, ?, ?, ?)""",
            (
                user["id"],
                user["login"],
                user["html_url"],
                user["repos_url"],
                user["type"],
            ),
        )
    connection.commit()
    connection.close()


def get_users(per_page=100, max_users=500):
    users = []
    since_id = 0

    while len(users) < max_users:
        url = "https://api.github.com/users"
        since_per_page = {"since": since_id, "per_page": per_page}

        response = requests.get(url, headers=autorization, params=since_per_page)

        if response.status_code == 200:
            batch_users = response.json()

        users.extend(batch_users)

        save_database(batch_users)

        since_id = batch_users[-1]["id"]

        time.sleep(0.200)

        with open("github_users.json", "w") as file:
            json.dump(users, file, indent=1)

    print(len(users))


make_database()
get_users()
