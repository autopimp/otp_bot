import os
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Replace 'your-bot-token' with your actual token from BotFather
BOT_TOKEN = "8101060602:AAH8BfgE6j24sz55ZYjYq2NwDZ9Gd2Dqg74"

@app.route('/bot', methods=['POST'])
def bot():
    update = request.get_json()
    chat_id = update['message']['chat']['id']
    
    if 'text' in update['message']:
        command = update['message']['text'].lower().strip()
        
        if command == '/start':
            send_otp(chat_id)
        elif command.startswith('/get-otp'):
            _, otp = command.split(' ')
            send_message(chat_id, f"Here is your OTP: {otp}")
    
    return jsonify({'ok': True})

def send_otp(chat_id):
    response = requests.get(f'http://localhost:5000/generate')
    if response.status_code == 200:
        otp = response.json()['otp']
        send_message(chat_id, f"Your OTP is {otp}")
    else:
        send_message(chat_id, "Failed to generate OTP")

def send_message(chat_id, text):
    url = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage'
    payload = {'chat_id': chat_id, 'text': text}
    requests.post(url, data=payload)

if __name__ == '__main__':
    app.run(port=5001)
