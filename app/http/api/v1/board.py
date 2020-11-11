from flask import request

from app.core.exceptions import InvalidRequestException

from app.http.api import api
from app.http.requests.board.create_board import CreateBoardRequestObject

from app.core.use_cases.create_board import CreateBoardUseCase

@api.route("/board")
def get_board():
    return "get board"


@api.route("/board", methods=["POST"])
def create_board():
    req = CreateBoardRequestObject.from_dict(a_dict=request.json)
    if not req:
        raise InvalidRequestException
    result = CreateBoardUseCase().excute()
    return request.json


@api.route("/board", methods=["DELETE"])
def delete_board():
    return "delete board"
