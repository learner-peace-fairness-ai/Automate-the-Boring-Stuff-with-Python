from imapclient import IMAPClient

with IMAPClient('imap.gmail.com', ssl=True) as client:
    print(client)
