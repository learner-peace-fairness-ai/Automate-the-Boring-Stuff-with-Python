# Usage: python 傘のリマインダー.py location openweathermap_API_KEY Twilio_account_sid Twilio_auth_token sms_from_number sms_to_number
from datetime import datetime
from datetime import timedelta
import json
import sys
import time

import requests
from twilio.rest import Client

URL = 'https://api.openweathermap.org/data/2.5/forecast'
LOCATION        = sys.argv[1]
# openweathermap
WEATHER_API_KEY = sys.argv[2]
# Twilio
TWILIO_ACCOUNT_SID = sys.argv[3]
TWILIO_AUTH_TOKEN  = sys.argv[4]
FROM_NUMBER = sys.argv[5]
TO_NUMBER   = sys.argv[6]


def get_weather():
    """OpenWeatherMap.orgから天気を取得する"""

    params = {
        'q': LOCATION,
        'cnt': 1,
        'appid': WEATHER_API_KEY
    }
    response = requests.get(URL, params=params)
    response.raise_for_status()

    weather_data = json.loads(response.text)
    w = weather_data['list']
    # w[0]['weather'][0] - {..., 'main': '天気', 'description': '天気の詳細', ...}
    # 雨なら main, descripiton に rain が含まれる
    return w[0]['weather'][0]['description']


def send_sms(message, from_number, to_number):
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    message = client.messages.create(
        body=message,
        from_=from_number,
        to=to_number
    )

def main():
    weather = get_weather()
    # 雨ならSMSに傘を忘れないようにメッセージ
    if 'rain' in weather:  # 雨なら rain が含まれる
        send_sms('雨なので傘を持っていく', FROM_NUMBER, TO_NUMBER)



# 毎日起床直前に実行する
next_run = datetime.now().replace(hour=6, minute=30, second=0)
while True:
    # 起床時間を過ぎていたら次回の実行時刻を再セット
    if datetime.now() > next_run:
        next_run += timedelta(days=1)

    wait_seconds = (next_run - datetime.now()).total_seconds()
    time.sleep(wait_seconds)
    main()
