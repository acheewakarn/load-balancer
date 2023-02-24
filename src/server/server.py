import os
from flask import Flask

def init_app(s):
    app = Flask(__name__)

    @app.route("/server/info")
    def server_info():
        return "Hello, World from server " + os.getenv("IPV4_ADDRESS")

    app.add_url_rule("/", endpoint="server_info")

    return app
