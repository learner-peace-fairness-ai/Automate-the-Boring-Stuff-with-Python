from smtplib import SMTP
import sys

FROM_ADDRESS = sys.argv[1]
TO_ADDRESS   = sys.argv[2]
APP_PASSWORD = sys.argv[3]

msg = '''Subject: So long.
Dear Alice, so long and thanks for all the fish.
Sincerelly, Bob'''

with SMTP('smtp.gmail.com', 587) as server:
    server.starttls()
    server.login(FROM_ADDRESS, APP_PASSWORD)
    server.sendmail(FROM_ADDRESS, TO_ADDRESS, msg)
