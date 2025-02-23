#! python3
# quickWeather.py - コマンドラインに指定した地名の天気予報を表示する

import json
import sys

import requests

URL = 'https://api.openweathermap.org/data/2.5/forecast'
# openweathermap.orgから取得したAPIキーを定義しておく
API_KEY = 'APIキー'

# コマンドライン引数から地名を組み立てる
if len(sys.argv) < 2:
    print('Usage: quickWeather.py location')
    sys.exit()
location = ' '.join(sys.argv[1:])

# OpenWeatherMap.orgのAPIからJSONデータをダウンロードする
params = {
    'q': location,
    'cnt': 3,
    'appid': API_KEY
}
response = requests.get(URL, params=params)
response.raise_for_status()

# JSONデータからPython変数に読み込む
weather_data = json.loads(response.text)
# 天気予報の情報を表示する
w = weather_data['list']
print(f'{location}の現在の天気:')
print(f'{w[0]['weather'][0]['main']} - {w[0]['weather'][0]['description']}')
print()

print('明日:')
print(f'{w[1]['weather'][0]['main']} - {w[1]['weather'][0]['description']}')
print()

print('明後日:')
print(f'{w[2]['weather'][0]['main']} - {w[2]['weather'][0]['description']}')
