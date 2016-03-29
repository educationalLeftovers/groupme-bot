import os
import random
from flask import Flask

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

if __name__ == "__main__":
	port = int(os.environ.get("PORT", 5000))
	# app.run(host='0.0.0.0', port=port, debug=True)
	app.run(host='0.0.0.0', port=port)
