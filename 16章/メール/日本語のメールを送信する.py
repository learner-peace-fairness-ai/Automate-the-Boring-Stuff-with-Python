from email.message import EmailMessage
from smtplib import SMTP
import sys

FROM_ADDRESS = sys.argv[1]
TO_ADDRESS   = sys.argv[2]
APP_PASSWORD = sys.argv[3]

msg = EmailMessage()
msg['From'] = FROM_ADDRESS
msg['To'] = TO_ADDRESS
msg['Subject'] = 'タイトル'
msg.set_content('本文')


with SMTP('smtp.gmail.com', 587) as server:
    server.starttls()
    server.login(FROM_ADDRESS, APP_PASSWORD)
    server.send_message(msg)
