from smtplib import SMTP
import sys

EMAIL_ADDRESS = sys.argv[1]
APP_PASSWORD  = sys.argv[2]

with SMTP('smtp.gmail.com', 587) as server:
    server.starttls()
    result = server.login(EMAIL_ADDRESS, APP_PASSWORD)
    print(result)
