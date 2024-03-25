import os
import requests
import random
import telegram
import time
from dotenv import load_dotenv


FIRST_COMIC = 1
LAST_COMIC = 2910


def download_image(image_url):
    response = requests.get(image_url)
    response.raise_for_status()
    return response.content


def save_image(image_content, filepath):
    with open(filepath, 'wb') as file:
        file.write(image_content)


def publish_image(tg_token, tg_chat_id, filepath, alt_text):
    bot = telegram.Bot(token=tg_token)
    with open(filepath, 'rb') as img:
        bot.send_photo(chat_id=tg_chat_id, photo=img, caption=alt_text)
    os.remove(filepath)


def fetch_and_publish_comic(comic_url, tg_token, tg_chat_id):
    response = requests.get(comic_url)
    response.raise_for_status()
    metadata = response.json()

    title = metadata["safe_title"]
    alt_text = metadata["alt"]
    image_url = metadata["img"]

    comic_number = metadata["num"]
    filename = f"xkcd_{comic_number}_{title}.png"

    image_content = download_image(image_url)

    filepath = os.path.join(os.getcwd(), filename)
    save_image(image_content, filepath)

    publish_image(tg_token, tg_chat_id, filepath, alt_text)


if __name__ == "__main__":
    load_dotenv()
    publish_interval = os.getenv("PUBLISH_INTERVAL")
    tg_token = os.getenv("TELEGRAM_TOKEN")
    tg_chat_id = os.getenv("TG_CHAT_ID")

    comic_number = random.randrange(FIRST_COMIC, LAST_COMIC)
    comic_url = f"https://xkcd.com/{comic_number}/info.0.json"

    fetch_and_publish_comic(comic_url, tg_token, tg_chat_id)

