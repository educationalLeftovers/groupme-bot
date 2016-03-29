import os
import random
from flask import Flask

from quotes import quotes

app = Flask(__name__)

@app.route('/hello')
def hello():
	return 'Hello world!'

@app.route('/'):
def trash():
	return(random.choose(quotes))

if __name__ == "__main__":
	port = int(os.environ.get("PORT", 5000))
	app.run(host='0.0.0.0', port=port)
