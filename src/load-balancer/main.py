import os
from flask import Flask
from requests import get

import random

app = Flask(__name__)

@app.route("/")
def hello_world(): 

    def getRandomServiceAddress():
        return random.choice(str.split((os.getenv("NODE-ADDRESSES")), ";"))

    service_address = getRandomServiceAddress()

    return get(service_address, verify=False).content
    # return get("https://example.com", verify=False, timeout=10).content

@app.route("/node-count")
def node_count():
    return os.getenv("NODE-COUNT")

@app.route("/node-addresses")
def node_addresses():
    return str.split((os.getenv("NODE-ADDRESSES")), ";")
