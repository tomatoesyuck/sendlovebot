import os
import random
from twilio.rest import Client
import schedule
import time

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']

client = Client(account_sid, auth_token)

def sendMsg():
    msgs = []
    with open("messages.txt") as f:
        msgs = f.readlines()

    randIndex = random.randint(0, len(msgs) - 1)
    chosenMsg = msgs[randIndex]

    message = client.messages \
        .create(
        body=chosenMsg,
        #19897046430
        from_='+19897046430',
        to='+19083918966'
    )

    print(message.sid)
    print(chosenMsg)


schedule.every().day.at("17:20").do(sendMsg)
schedule.every().day.at("05:20").do(sendMsg)

while 1: #not running sendMsg
    schedule.run_pending()
    time.sleep(1)
