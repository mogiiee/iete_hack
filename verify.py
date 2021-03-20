from flask import Flask, request, render_template
from twilio.rest import Client
import random

app = Flask(__name__)
app.secret_key = 'otp'


@app.route('/')
def home():
    return render_template('/login.html')


@app.route('/getOTP', methods=['POST'])
def getOTP():
    number = request.form['number']
    val = getOTPApi(number)
    if val:
        return render_template('enterOTP.html')


@app.route('/ValidateOTP', methods=['POST'])
def validateOTP():
    otp = request.form['otp']
    if "response" in session:
        s = session['response']
        session.pop('response', None)
        if s == otp:
            return "you are auth, talk to the doc "
        else:
            return "wrong otp try again"


session = {}


def generateOTP():
    return random.randrange(100000, 999999)


def getOTPApi(number):
    ssid = ''' i'll enter when needed'''
    auth_token = ''' i'll enter when needed'''
    client = Client(ssid, auth_token)
    otp = generateOTP()
    session['response'] = str(otp)
    body = 'your otp is' + str(otp)
    message = client.messages.create(
        from_='+18102165316',
        body=body,
        to=number
    )
    if message.sid:
        return True
    else:
        False


if __name__ == "__main__":
    app.run(debug=True)
