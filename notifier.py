import requests

def send_discord(webhook_url, patch):

    embed = {
        "title": "🍁 메이플 플래닛 패치노트",
        "description": f"**{patch['title']}**",
        "url": patch["url"],
        "color": 3066993,
        "footer": {
            "text": "MaplePlanetNotifier"
        }
    }

    data = {
        "embeds": [embed]
    }

    response = requests.post(webhook_url, json=data)

    if response.status_code in (200, 204):
        print("Discord 전송 성공")
    else:
        print("Discord 전송 실패")
        print(response.status_code)
        print(response.text)
