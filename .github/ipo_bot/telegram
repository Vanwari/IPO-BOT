import os, requests

def send_message(text):
    token=os.environ['TELEGRAM_BOT_TOKEN']; chat_id=os.environ['TELEGRAM_CHAT_ID']
    r=requests.post(f'https://api.telegram.org/bot{token}/sendMessage',json={'chat_id':chat_id,'text':text,'parse_mode':'HTML'},timeout=30)
    r.raise_for_status()
