import os
import random
from flask import Flask, json, request
import requests


from quotes import quotes

app = Flask(__name__)

@app.route('/hello')
def hello():
	return 'Hello world!'

@app.route('/')
def trash():
	return(random.choice(quotes))

@app.route('/test')
def test():
	return(os.environ.get("CONFIG_ITEM", '(failed to get config item)'))

@app.route('/callback/', methods=['POST'])
def groupme_callback():
	json_body = request.get_json()
	if json_body['group_id'] == os.environ['GROUP_ID']:
		# some degree of verification that it is sent via a groupme callback
		# could also check for "User-Agent: GroupMeBotNotifier/1.0", but that's plenty spoofable

		if 'trash' in json_body['text']:
			payload = {
				'bot_id' : os.environ['BOT_ID'],
				'text'   : random.choice(quotes),
			}
			requests.post('https://api.groupme.com/v3/bots/post', json=payload)
			return('ok, trash\n')
		return('ok, no trash\n')

if __name__ == "__main__":
	port = int(os.environ.get("PORT", 5000))
	# app.run(host='0.0.0.0', port=port, debug=True)
	app.run(host='0.0.0.0', port=port)
