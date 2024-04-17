from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "welcome to voting"


@app.route('/user')
def getUser():
    return (1,2,2)
