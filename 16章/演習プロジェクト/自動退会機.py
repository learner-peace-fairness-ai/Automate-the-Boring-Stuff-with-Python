# Usage: python 自動退会機.py gmail_address app_password
import email
from email.parser import BytesParser
import re
import sys
from typing import Union
import webbrowser

from bs4 import BeautifulSoup
from imapclient import IMAPClient


def get_email_body_html(mail: Union[email.message.EmailMessage, email.message.Message]):
    html_contents = []
    for part in mail.walk():
        # 添付ファイルをスキップ
        content_disposition = part.get('Content-Disposition')
        if content_disposition == 'attachment':
            continue

        content_type = part.get_content_type()
        content_encoding = part.get_content_charset() or 'utf-8'
        if content_type == 'text/html':
            html_contents.append(part.get_payload(decode=True).decode(content_encoding, errors='replace'))

    if html_contents:
        return '\n'.join(html_contents)
    else:
        return ''


def get_unsubscribe_link(html):
    soup = BeautifulSoup(html, 'html.parser')
    unsubscribe_link = soup.find('a', string=re.compile('unsubscribe'))
    if unsubscribe_link:
        return unsubscribe_link.get('href')
    else:
        return ''


EMAIL_ADDRESS = sys.argv[1]
APP_PASSWORD  = sys.argv[2]

with IMAPClient('imap.gmail.com', ssl=True) as client:
    client.login(EMAIL_ADDRESS, APP_PASSWORD)
    client.select_folder('INBOX')
    # 全メールを取得する
    uid_list = client.search()

    raw_messages = client.fetch(uid_list, ['BODY[]'])
    for uid in uid_list:
        raw_email = raw_messages[uid][b'BODY[]']
        mail = BytesParser().parsebytes(raw_email)

        html = get_email_body_html(mail)
        url = get_unsubscribe_link(html)

        if url:
            webbrowser.open(url)
