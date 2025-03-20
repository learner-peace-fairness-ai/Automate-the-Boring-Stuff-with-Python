import time
import sys

from twilio.rest import Client

ACCOUNT_SID = sys.argv[1]
AUTH_TOKEN  = sys.argv[2]
FROM_NUMBER = sys.argv[3]
TO_NUMBER   = sys.argv[4]

client = Client(ACCOUNT_SID, AUTH_TOKEN)
message = client.messages.create(
    body='ワトソン君、用事がある、ちょっと来てくれたまえ。',
    from_=FROM_NUMBER,
    to=TO_NUMBER
)

print(message.to)
print(message.from_)
print(message.body)

print(message.status)
print(message.date_created)
print(message.date_sent == None)

time.sleep(1)

message_id = message.sid
print(message_id)
updated_message = client.messages.get(message_id).fetch()
print(updated_message.status)
print(updated_message.date_sent)
