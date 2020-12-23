from flask import request
from http import HTTPStatus

from app.core.exceptions import InvalidRequestException

from app.http.api import api
from app.http.requests.board.create_board import CreateBoardRequestObject

from app.core.use_cases.v1.board.create_board import CreateBoardUseCase
from app.core.use_cases.v1.board.delete_board import DeleteBoardUseCase

from app.core.dto.board import CreateBoardDto


@api.route("/boards")
def get_board():
    return "get board"


@api.route("/boards", methods=["POST"])
def create_board():
    req = CreateBoardRequestObject.from_dict(a_dict=request.json)

    if not req:
        raise InvalidRequestException(req.get_error_msg(), HTTPStatus.BAD_REQUEST)

    dto = CreateBoardDto(**req.to_dict())

    result = CreateBoardUseCase().execute(dto)

    if not result:
        raise InvalidRequestException(result.type.msg, result.type.code)
    return request.json


@api.route("/boards/<int:board_id>", methods=["DELETE"])
def delete_board(board_id):
    result =
    return "delete board"
