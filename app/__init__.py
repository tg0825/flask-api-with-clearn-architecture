from flask import Flask, Blueprint
from app.config import config
from app.http.api import api as api_bp

main = Blueprint("main", __name__)


@main.route("/")
def index():
    return "main"


def init_blueprint(app):
    app.register_blueprint(main)
    app.register_blueprint(api_bp, url_prefix="/api")


def create_app(config_name="default"):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    with app.app_context():
        init_blueprint(app)

    return app
