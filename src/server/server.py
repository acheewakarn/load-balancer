from flask import Flask

def init_app(serverId):
    app = Flask(__name__)

    @app.route("/server/info")
    def server_info():
        return str(serverId)

    app.add_url_rule("/", endpoint="server_info")

    return app