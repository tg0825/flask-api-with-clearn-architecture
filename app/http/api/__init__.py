from flask import Blueprint, jsonify

api: Blueprint = Blueprint(
    "api",
    __name__,
)

from app.http.api.v1.board import *


@api.errorhandler(InvalidRequestException)
def handle_invalid_request(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response
