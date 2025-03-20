import pprint
import sys

from imapclient import IMAPClient

EMAIL_ADDRESS = sys.argv[1]
APP_PASSWORD  = sys.argv[2]

with IMAPClient('imap.gmail.com', ssl=True) as client:
    client.login(EMAIL_ADDRESS, APP_PASSWORD)
    pprint.pprint(client.list_folders())    

    result = client.select_folder('INBOX', readonly=True)
    print(result)
