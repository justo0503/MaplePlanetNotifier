from parser import get_latest_patch
from notifier import send_discord

WEBHOOK_URL = https://discord.com/api/webhooks/1520105869948227585/yVlojPgb0A2YpQAcxEfkGIBJrZEZZuoSPRSBpR3-UNPLX1rQl-iOaNemTGxXbrdq9h_w

latest = get_latest_patch()

if latest:
    send_discord(WEBHOOK_URL, latest)
