from flask import Blueprint

api: Blueprint = Blueprint(
    "api",
    __name__,
)

from app.http.api.v1.board import *