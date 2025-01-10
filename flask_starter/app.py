from flask import Flask, request
from markupsafe import escape
from datetime import datetime
import socket

app = Flask(__name__)

visits = 0 # Init gobal
STYLE = " NATIVE(1) "

@app.route("/")
def default():
    global visits # Grab visits from 'global' 
    visits +=1 # Increment +11
    now = datetime.now()
    myNAME=socket.gethostname()
    myHOST=request.headers.get('Host')
    if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
        theirADDR=request.remote_addr
        theirPORT=request.environ.get('REMOTE_PORT')

    else:
        theirADDR=request.environ['HTTP_X_FORWARDED_FOR']
        theirADDR=request.environ['PORT']  ## Does not work if behind proxy... 
    
    timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
    return timestamp + STYLE + myNAME + "(" + myHOST + ")"+ " " + str(visits) +  ". From " + theirADDR + ":" +  str(theirPORT) + "!\n" # Return string with more info

@app.route("/hello")
def hello_world():
    return "Hello World!"

@app.route("/another")
def another():
    return "Another Hello World!"

@app.route("/dynamic/<name>")
def dynamic(name):
    return f"Hello {escape(name)}"

@app.route("/json/<name>")
def json(name):
    return {
        "data": {
            "name": name
        }
    }
