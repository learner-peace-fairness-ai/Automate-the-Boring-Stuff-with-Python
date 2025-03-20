# 15分おきにメールチェックして、命令メールを見つけたら本文を表示するタスクを実行する
# 命令メールにはパスワードが含まれている
# タスクが完了したらメールを自分宛に送り、命令メールを削除する
# Usage: python メールを使ってコンピュータを制御する.py email_address app_password order_password
from datetime import datetime
from datetime import timedelta
import email
from email.parser import BytesParser
from email.header import decode_header
from email.message import EmailMessage
from email.utils import parseaddr
import logging
from logging import FileHandler
from logging import Formatter
from logging import StreamHandler
from pathlib import Path
from smtplib import SMTP
import sys
from threading import Thread
import time
from typing import Union

from imapclient import IMAPClient

ORDER_MAIL_TITLE = '命令メール'
LOG_FILE = Path('メールを使ってコンピュータを制御する.log')
LOG_FORMAT = '(%(levelname)s) [%(asctime)s] %(message)s'

formatter = Formatter(LOG_FORMAT)

console_handler = StreamHandler()
console_handler.setFormatter(formatter)

file_handler = FileHandler(LOG_FILE, encoding='utf-8')
file_handler.setFormatter(formatter)

logging.basicConfig(
    level=logging.INFO,
    handlers=[console_handler, file_handler],
    datefmt='%Y/%m/%d %H:%M:%S'
)


def get_email(client, mail_id) -> (Union[email.message.EmailMessage, email.message.Message]):
    raw_message = client.fetch(mail_id, ['BODY[]'])
    raw_email = raw_message[mail_id][b'BODY[]']
    return BytesParser().parsebytes(raw_email)


def get_email_body_text(mail: Union[email.message.EmailMessage, email.message.Message]):
    text_contents = []
    for part in mail.walk():
        # 添付ファイルをスキップ
        content_disposition = part.get('Content-Disposition')
        if content_disposition == 'attachment':
            continue

        content_type = part.get_content_type()
        content_encoding = part.get_content_charset() or 'utf-8'
        if content_type == 'text/plain':
            text_contents.append(part.get_payload(decode=True).decode(content_encoding, errors='replace'))

    if text_contents:
        return '\n'.join(text_contents)
    else:
        return ''


def get_email_subject(mail: Union[email.message.EmailMessage, email.message.Message]):
    subject, encoding = decode_header(mail['Subject'])[0]
    if isinstance(subject, bytes):
        subject = subject.decode(encoding if encoding else 'utf-8')
    return subject


# 命令メールがあるかチェックして命令メールのメールIDのリストを返す
def get_order_gmail_id_list(email_address, app_password, order_password):
    order_mail_id = []
    with IMAPClient('imap.gmail.com', ssl=True) as client:
        client.login(email_address, app_password)
        client.select_folder('INBOX')
        uid_list = client.search()

        for uid in uid_list:
            mail = get_email(client, uid)

            # 命令メールを探す
            subject = get_email_subject(mail)
            if subject != ORDER_MAIL_TITLE:
                continue
            
            # メールが自分から送信されたものであることを確認
            _, from_address = parseaddr(mail['From'])
            if from_address != email_address:
                continue

            text = get_email_body_text(mail)
            # パスワードを確認する (本文1行目にパスワードがある)
            lines = text.splitlines()
            password_line = lines[0]
            if is_order_password(password_line, order_password):
                order_mail_id.append(uid)
    return order_mail_id


# 命令メール内の命令のリストを返す
def get_orders(email_address, app_password, uid_list):
    orders = []
    with IMAPClient('imap.gmail.com', ssl=True) as client:
        client.login(email_address, app_password)
        client.select_folder('INBOX')

        for uid in uid_list:
            mail = get_email(client, uid)
            text = get_email_body_text(mail)
            
            lines = text.splitlines()
            order_text = '\n'.join(lines[1:])  # 本文1行目のパスワード行を除外
            orders.append(order_text)
    return orders


# password_lineのフォーマット: "PASSWORD:パスワード"
def is_order_password(password_line, order_password):
    password = password_line.split(':')[1]
    return password == order_password


def print_order(msg):
    print(msg)


def send_gmail(msg: email.message.EmailMessage, app_password):
    with SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(msg['From'], app_password)
        server.send_message(msg)


def delete_gmails(email_address, app_password, id):
    with IMAPClient('imap.gmail.com', ssl=True) as client:
        client.login(email_address, app_password)
        client.select_folder('INBOX')
        client.delete_messages(id)


def main(email_address, app_password, order_password):
    logging.info('main()開始')
    logging.info('メールチェックを実行します。')
    order_mail_id_list = get_order_gmail_id_list(email_address, app_password, order_password)
    if not order_mail_id_list:
        logging.info('命令メールは見つかりませんでした。')
        logging.info('main()終了')
        return

    logging.info(f'orderが{len(order_mail_id_list)}件見つかりました。')

    orders = get_orders(email_address, app_password, order_mail_id_list)
    print_threads = {}
    for order in orders:
        print_thread = Thread(target=print_order, args=[order])
        print_threads[order] = print_thread

    for order in print_threads:    
        logging.info(f'order: "{order}" を実行します。')
        print_threads[order].start()
    
    for order in print_threads:
        print_threads[order].join()
        logging.info(f'order: "{order}" が完了しました。')
        
        msg = EmailMessage()
        msg['From']    = email_address
        msg['To']      = email_address
        msg['Subject'] = '命令完了'
        msg.set_content(f'order: {order} を実行しました。')
        send_gmail(msg, app_password)
        logging.info('完了メールを送信しました。')

    delete_gmails(email_address, app_password, order_mail_id_list)
    logging.info('命令メールをすべて削除しました。')
    logging.info('main()終了')


EMAIL_ADDRESS  = sys.argv[1]
APP_PASSWORD   = sys.argv[2]
ORDER_PASSWORD = sys.argv[3]

# 15分おきにmain()を実行
next_run = datetime.now()
while True:
    # 次回の実行時刻を再セット
    next_run += timedelta(minutes=15)

    try:
        main(EMAIL_ADDRESS, APP_PASSWORD, ORDER_PASSWORD)
    except Exception as e:
        logging.error('例外が発生しました', exc_info=True)

    wait_seconds = (next_run - datetime.now()).total_seconds()
    time.sleep(wait_seconds)
