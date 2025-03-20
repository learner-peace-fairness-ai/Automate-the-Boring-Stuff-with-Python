from smtplib import SMTP

with SMTP('smtp.gmail.com', 587) as server:
    server.ehlo()
    result = server.starttls()
    print(result)
