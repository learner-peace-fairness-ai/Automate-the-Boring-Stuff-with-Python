# Usage: python 雑用ランダム割り当てメーラー.py from, app_password, "作業者メールアドレス1, ..." "雑用1, ..."
from collections import defaultdict
from datetime import datetime
from datetime import timedelta
from email.message import EmailMessage
import random
from smtplib import SMTP
import sys
import time

FROM_ADDRESS = sys.argv[1]
APP_PASSWORD = sys.argv[2]

latest_chore_db = defaultdict(str)  # メールアドレス: 前回の雑用


def get_random_chore(chores, latest_chore):
    assignable_chores = [x for x in chores if x != latest_chore]
    return random.choice(assignable_chores)


def send_message(chore, to_address):
    msg = EmailMessage()
    msg['From'] = FROM_ADDRESS
    msg['To'] = to_address
    msg['Subject'] = '雑用'
    msg.set_content(f'今週の雑用は{chore}です。')

    with SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(FROM_ADDRESS, APP_PASSWORD)
        server.send_message(msg)


def main(mail_addresses, chores):
    worker_addresses = mail_addresses.copy()
    remaining_chores = chores.copy()

    random.shuffle(worker_addresses)
    for mail_address in worker_addresses:
        assigned_chore = get_random_chore(remaining_chores, latest_chore_db[mail_address])
        remaining_chores.remove(assigned_chore)

        # 雑用をメールする
        send_message(assigned_chore, mail_address)
        
        latest_chore_db[mail_address] = assigned_chore
    

mail_addresses = [s.strip() for s in sys.argv[3].split(',')]
chores         = [s.strip() for s in sys.argv[4].split(',')]

# 週に1度実行する
next_run = datetime.now()
while True:
    main(mail_addresses, chores)
    next_run += timedelta(days=7)
    wait_seconds = (next_run - datetime.now()).total_seconds()
    time.sleep(wait_seconds)
