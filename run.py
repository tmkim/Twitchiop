from flask import Flask
import requests
from flask import redirect
import twilio.twiml
from twilio.rest import  TwilioRestClient
import vid2aud
import boto
import os
import urllib2

app = Flask(__name__)
# Try adding your own number to this list!
callers = {
"+14158675309": "Curious George",
"+14158675310": "Boots",
"+14158675311": "Virgil",
"+17327964267": "Tames"
}
account_sid = "ACd04a3d6d646809d8e2aafa609e03d38d"
auth_token = "dae02b5d7c0b54b3fae7aa05560c1d81"
client = TwilioRestClient(account_sid, auth_token)

@app.route("/", methods=['GET', 'POST'])
def hello():
	"""Respond and greet the caller by name"""
	msg = request.values.get('Body', None)
	num = request.values.get('From', None)
	#message = vid2aud.vid2mp3(vid2aud.getVidFile(vid2aud.getVidId(msg)))
	
	call = client.calls.create(to=num, from_="+13472526162", url="http://tmkim.github.io/workplz")	
	resp = twilio.twiml.Response()
	resp.message(message)
	return str(resp)

if __name__ == "__main__":
	app.run(debug=True)
