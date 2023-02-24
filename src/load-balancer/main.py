import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/service-info")
def service_info():
    return os.environ("SERVICE-PORT")