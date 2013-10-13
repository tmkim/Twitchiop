# Download the Python helper library from twilio.com/docs/python/install
from twilio.rest import TwilioRestClient

def call():
	rec = raw_input("Your number: ")

	# Your Account Sid and Auth Token from twilio.com/user/account
	account_sid = "ACd04a3d6d646809d8e2aafa609e03d38d"
	auth_token = "dae02b5d7c0b54b3fae7aa05560c1d81"
	client = TwilioRestClient(account_sid, auth_token)

	call = client.calls.create(url="http://tmkim.github.io/workplz",
		to=rec,
		from_="+13472526162")

def main():
	call()
	print "note: this demo won't start for 36 seconds.. just because that's how long day9      decided to wait before putting on pre-game music"

if __name__ == '__main__':
	main()
