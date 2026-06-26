import time

from parser import get_latest_patch
from notifier import send_discord
from storage import get_last_post, save_last_post
from config import WEBHOOK_URL, CHECK_INTERVAL


def check():

    latest = get_latest_patch()

    if latest is None:
        print("패치노트를 읽지 못했습니다.")
        return

    last = get_last_post()

    if latest["id"] == last:
        print("새 패치노트 없음")
        return

    print("새 패치노트 발견!")

    send_discord(WEBHOOK_URL, latest)

    save_last_post(latest["id"])


if __name__ == "__main__":

    print("MaplePlanetNotifier 시작")

    while True:

        try:
            check()

        except Exception as e:
            print(e)

        time.sleep(CHECK_INTERVAL)
