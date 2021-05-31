import os

from flask import Flask
from flask_adminlte import AdminLTE
from flask_sqlalchemy import SQLAlchemy
from flask_sslify import SSLify

db = SQLAlchemy()


def create_app(environment: str):
    app = Flask(__name__)
    app.config["SECRET_KEY"] = os.getenv("SECRET", "secret")
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ["DB_HOST"]
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SQLALCHEMY_ECHO"] = True

    # initialize apps
    AdminLTE(app)
    db.init_app(app)

    if environment != "dev":
        SSLify(app)

    # register blueprints
    from app.routes import app as seller_app

    app.register_blueprint(seller_app)

    return app
