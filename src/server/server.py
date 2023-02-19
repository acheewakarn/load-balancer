from flask import Flask

def init_app(s):
    app = Flask(__name__)

    @app.route("/server/info")
    def server_info():
        return "Message from server #" + str(s)

    app.add_url_rule("/", endpoint="server_info")

    return app
