import json

import requests


def get_users_by_id_define_per_page(since_id=0, per_page=30):
    url_users = f"https://api.github.com/users?since={since_id}&per_page={per_page}"
    return url_users


response = requests.get(get_users_by_id_define_per_page())


if response.status_code == 200:
    users_info = response.json()
    if len(users_info) == 0:
        raise Exception("No users found, please, try again.")
    with open("github_users.json", "w") as file:
        json.dump(users_info, file, indent=1)
    print(f"Got {len(users_info)} users")
else:
    raise Exception(f"Response failed, got HTTP code: {response.status_code}")
