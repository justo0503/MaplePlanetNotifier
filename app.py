import requests
from bs4 import BeautifulSoup

URL = "https://mapleplanet.co.kr/board/update"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(URL, headers=headers)

print(response.status_code)

soup = BeautifulSoup(response.text, "lxml")

print(soup.title.text)
