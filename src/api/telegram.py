import requests
import json

url = 'https://api.telegram.org/bot'
token = '5498402431:AAE2E-MBAZuUktFZq71pIjtmB8sKxY4u6r8'

def sendMessage(chat_id, text, buttons = None):
  url = 'https://api.telegram.org/bot' + token + '/sendMessage'
  data = {'chat_id': chat_id, 'text': text}
  if buttons is not None:
    data['reply_markup'] = json.dumps({'inline_keyboard': buttons})
  requests.post(url, data=data)

def updateMessage(chat_id, message_id, text, buttons = None):
  url = 'https://api.telegram.org/bot' + token + '/editMessageText'
  data = {'chat_id': chat_id, 'message_id': message_id, 'text': text}
  if buttons is not None:
    data['reply_markup'] = json.dumps({'inline_keyboard': buttons})
  requests.post(url, data=data)
