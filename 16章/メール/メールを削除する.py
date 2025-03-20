import sys

from imapclient import IMAPClient

EMAIL_ADDRESS = sys.argv[1]
APP_PASSWORD  = sys.argv[2]

with IMAPClient('imap.gmail.com', ssl=True) as client:
    client.login(EMAIL_ADDRESS, APP_PASSWORD)
    client.select_folder('INBOX')
    UIDs = client.search(['ALL'])
    if not UIDs:
        sys.exit()
    
    latest_uid = max(UIDs)
    result = client.delete_messages([latest_uid])
    print(result)

    result = client.expunge()  # GMailはdelete_messages()の時点で完全削除される
    print(result)
