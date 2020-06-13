import redis
import os
from flask import Flask, request, render_template, session
from flask_session import Session
from flask_cors import CORS
from source import main


app = Flask(__name__)
CORS(app)
app.config['DEBUG'] = True

#SESSION_TYPE = 'redis'
#SESSION_PERMANENT = False
#SESSION_REDIS = redis.from_url(os.environ.get("REDIS_URL"))
#REDIS_URL = 'localhost:8080'

app.config.from_object(__name__)

app.secret_key = b'watermelon'

#Session(app)
"""
session['key'] = value
"""


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html', game=main.game)


if __name__ == '__main__':
    app.run(threaded=True, port=5000)
