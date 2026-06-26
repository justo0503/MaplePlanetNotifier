import json
import os

DATA_FILE = "data/last_post.json"


def get_last_post():
    if not os.path.exists(DATA_FILE):
        return ""

    with open(DATA_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    return data.get("id", "")


def save_last_post(post_id):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(
            {"id": post_id},
            f,
            ensure_ascii=False,
            indent=4
        )
