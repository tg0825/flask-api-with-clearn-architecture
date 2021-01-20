from flask import Flask, Blueprint
from app.config import config
from app.extensions.database import db, ma
from app.extensions.provider import init_provider

from flask_bcrypt import Bcrypt

# 이게 위에 있으면 안됨
from app.http.api import api as api_bp

main = Blueprint("main", __name__)


@main.route("/")
def index():
    return "main"


def init_db(app):
    db.init_app(app)


def init_marshmallow(app):
    ma.init_app(app)


def init_blueprint(app):
    app.register_blueprint(main)
    app.register_blueprint(api_bp, url_prefix="/api")


def create_app(config_name="default"):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    app.secret_key = "!!!!!!"
    bcrypt = Bcrypt(app)

    with app.app_context():
        init_db(app)
        init_blueprint(app)
        init_provider(app)
        init_marshmallow(app)

    return app
