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
