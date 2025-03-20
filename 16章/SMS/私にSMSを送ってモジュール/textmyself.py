#! python3
# textmyself.py - 引数の文字列をSMSで送信巣sるtext_myself()を定義する

import sys

from twilio.rest import Client

# 設定値
ACCOUNT_SID = sys.argv[1]
AUTH_TOKEN  = sys.argv[2]
FROM_NUMBER = sys.argv[3]  # 購入した米国の電話番号
TO_NUMBER   = sys.argv[4]  # 自分の携帯番号

def text_myself(message):
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    client.messages.create(
        body=message,
        from_=FROM_NUMBER,
        to=TO_NUMBER
    )
