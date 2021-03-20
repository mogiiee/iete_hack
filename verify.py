import random  # generate random number
from twilio.rest import Client
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('phone_verification.html')


otp = random.randint(100000, 999999)
print("Your OTP is - ", otp)
# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'AC69f62dfca2244ab12c4c405908493828'
auth_token = '426792209806bec4d7e7288e0191a0eb'
client = Client(account_sid, auth_token)

message = client.messages.create(
    body='Hello Mr. Mayur Your Secure Device OTP is - ' +
    str(otp) + 'now your mobile is hacked!\n Byby...',
    from_='+18102165316',
    to='+917013764661'
)

print(message.sid)
