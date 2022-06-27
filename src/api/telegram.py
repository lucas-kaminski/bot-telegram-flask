import requests
import json

url = "https://api.telegram.org/bot"
token = "5498402431:AAE2E-MBAZuUktFZq71pIjtmB8sKxY4u6r8"


def setWebhook(url_webhook):
    url = "https://api.telegram.org/bot" + token + "/setWebhook"
    data = {"url": url_webhook, "drop_pending_updates": True}
    requests.post(url, data=data)


def setCommands():
    with open("src/json/commands.json") as json_file:
        commands = json.load(json_file)
    url = "https://api.telegram.org/bot" + token + "/setMyCommands"
    data = {"commands": commands}
    requests.post(url, data=data)


def sendMessage(chat_id, text, buttons=None, parse_mode="Markdown"):
    url = "https://api.telegram.org/bot" + token + "/sendMessage"
    data = {"chat_id": chat_id, "text": text, "parse_mode": parse_mode}
    if buttons is not None:
        data["reply_markup"] = json.dumps({"inline_keyboard": buttons})
    try:
        requests.post(url, data=data)
    except Exception as e:
        print(e)
        print("Error: unable to send message")


def updateMessage(chat_id, message_id, text, buttons=None, parse_mode="Markdown"):
    url = "https://api.telegram.org/bot" + token + "/editMessageText"
    data = {
        "chat_id": chat_id,
        "message_id": message_id,
        "text": text,
        "parse_mode": parse_mode,
    }
    if buttons is not None:
        data["reply_markup"] = json.dumps(
            {"inline_keyboard": buttons},
        )
    print(data)
    try:
        requests.post(url, data=data)
    except Exception as e:
        print(e)
        print("Error: unable to update message")


def deleteMessage(chat_id, message_id):
    url = "https://api.telegram.org/bot" + token + "/deleteMessage"
    data = {"chat_id": chat_id, "message_id": message_id}
    requests.post(url, data=data)


def sendPhoto(chat_id, photo, caption=None, buttons=None, parse_mode="Markdown"):
    url = "https://api.telegram.org/bot" + token + "/sendPhoto"
    data = {"chat_id": chat_id, "photo": photo, "parse_mode": parse_mode}
    if caption is not None:
        data["caption"] = caption
    if buttons is not None:
        data["reply_markup"] = json.dumps({"inline_keyboard": buttons})
    try:
        requests.post(url, data=data)
    except Exception as e:
        print(e)
        print("Error: unable to send photo")
