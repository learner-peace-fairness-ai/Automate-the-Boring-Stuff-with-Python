from email.header import decode_header
from email.parser import BytesParser
from email.utils import parseaddr
import sys

from imapclient import IMAPClient


EMAIL_ADDRESS = sys.argv[1]
APP_PASSWORD  = sys.argv[2]

with IMAPClient('imap.gmail.com', ssl=True) as client:
    client.login(EMAIL_ADDRESS, APP_PASSWORD)
    client.select_folder('INBOX', readonly=True)
    UIDs = client.search(['SINCE', '04-Mar-2025'])
    if not UIDs:
        sys.exit()
    raw_messages = client.fetch(UIDs, ['BODY[]'])
    latest_uid = max(UIDs)
    raw_email = raw_messages[latest_uid][b'BODY[]']
    mail = BytesParser().parsebytes(raw_email)
    
    text_contents = []
    html_contents = []
    for part in mail.walk():
        # 添付ファイルをスキップ
        content_disposition = part.get('Content-Disposition')
        if content_disposition == 'attachment':
            continue

        content_type = part.get_content_type()
        content_encoding = part.get_content_charset() or 'utf-8'
        if content_type == 'text/plain':
            text_contents.append(part.get_payload(decode=True).decode(content_encoding, errors='replace'))
        elif content_type == 'text/html':
            html_contents.append(part.get_payload(decode=True).decode(content_encoding, errors='replace'))
    
    if text_contents:
        print('\n'.join(text_contents))
    
    if html_contents:
        print('\n'.join(html_contents))
