from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

db: SQLAlchemy = SQLAlchemy()
session = db.session
ma = Marshmallow()
