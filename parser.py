import requests
from bs4 import BeautifulSoup

URL = "https://mapleplanet.co.kr/board/update"

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}


def get_latest_patch():

    response = requests.get(URL, headers=HEADERS)

    response.raise_for_status()

    soup = BeautifulSoup(response.text, "lxml")

    link = soup.find(
        "a",
        href=lambda x: x and "/board/update/" in x
    )

    if not link:
        return None

    title = link.get_text(strip=True)

    href = "https://mapleplanet.co.kr" + link["href"]

    post_id = link["href"].split("/")[-1]

    return {
        "id": post_id,
        "title": title,
        "url": href
    }


if __name__ == "__main__":

    latest = get_latest_patch()

    print(latest)
