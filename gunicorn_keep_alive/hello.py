import time

from flask import Flask


app = Flask(__name__)


@app.route("/")
def index():
    time.sleep(1)    
    return "hello world"
