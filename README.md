# Comics Publisher

This Python script automates the fetching and publishing of XKCD comics to a Telegram bot.
It downloads a random XKCD comic from the [XKCD website](https://xkcd.com/) and publishes it along with its alt text to a specified Telegram bot. 
The script utilizes the [XKCD JSON interface](https://xkcd.com/json.html) to fetch comic metadata and images.


## How to install

Python3 should already be installed. Then use pip (or pip3, if there is a conflict with Python2) to install dependencies:

```bash
pip install -r requirements.txt
```

A Telegram channel where you have administrative privileges. You'll need the chat ID for this channel.

### Obtain Telegram Bot Token

Create a Telegram bot using [BotFather](https://t.me/botfather) and obtain an API token for your bot.

### Configuration

Create a .env file in the project's root directory.

Add the following environment variables:

```bash
TELEGRAM_TOKEN=YOUR_TELEGRAM_BOT_TOKEN
TG_CHAT_ID=YOUR_CHANNEL_ID
PUBLISH_INTERVAL=24
```

YOUR_TELEGRAM_BOT_TOKEN with your Telegram bot's API token, 

YOUR_CHANNEL_ID with your Telegram channel's ID, and

PUBLISH_INTERVAL with your desired publication interval (default is 24 hours).

## How to run Scripts

To use this script, run the following command:

```bash
python fetch_and_publish_comics.py
```

## Project Goals
The code is written for educational purposes on online-course for web-developers, dvmn.org.



