from smtplib import SMTP

with SMTP('smtp.gmail.com', 587) as server:
    result = server.ehlo()
    print(result)
