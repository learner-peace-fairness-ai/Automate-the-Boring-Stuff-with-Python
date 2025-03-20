from email.header import decode_header
from email.parser import BytesParser
from email.utils import parseaddr
import sys

from imapclient import IMAPClient

EMAIL_ADDRESS = sys.argv[1]
APP_PASSWORD  = sys.argv[2]

with IMAPClient('imap.gmail.com', ssl=True) as client:
    result = client.login(EMAIL_ADDRESS, APP_PASSWORD)
    print(result)

    result = client.select_folder('INBOX', readonly=True)
    print(result)

    UIDs = client.search(['SINCE', '03-Mar-2025'])
    print(UIDs)
    
    if not UIDs:
        sys.exit()
    
    latest_uid = max(UIDs)
    raw_messages = client.fetch([latest_uid], ['BODY[]', 'FLAGS'])
    raw_email = raw_messages[latest_uid][b'BODY[]']
    mail = BytesParser().parsebytes(raw_email)

    subject, encoding = decode_header(mail['Subject'])[0]
    if isinstance(subject, bytes):
        subject = subject.decode(encoding if encoding else 'utf-8')
    print(subject)
    
    name_from, email_from = parseaddr(mail['From'])
    print(email_from)

    name_to, email_to = parseaddr(mail['To'])
    print(email_to)

    print(mail['Cc'])
    print(mail['Bcc'])
    
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
