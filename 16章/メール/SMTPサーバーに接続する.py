from smtplib import SMTP
from smtplib import SMTP_SSL

with SMTP('smtp.gmail.com', 587) as server_tls:
    print(type(server_tls))

with SMTP_SSL('smtp.gmail.com', 465) as server_ssl:
    print(type(server_ssl))
