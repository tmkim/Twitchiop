from flask import Flask, request, redirect
import twilio.twiml

app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
def rec():

	num = request.values.get('From', None)
	msg = request.values.get('Body', None)

	return num + "," + msg

if __name__ == "__main__":
	app.run(debug=True)

