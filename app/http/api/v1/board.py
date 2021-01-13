from flask import request
from http import HTTPStatus

from app.core.exceptions import InvalidRequestException

from app.http.api import api
from app.http.requests.v1.board import (
    CreateBoardRequestObject,
    DeleteBoardRequestObject,
    GetBoardListRequestObject,
)

from app.core.use_cases.v1.board.create_board import CreateBoardUseCase
from app.core.use_cases.v1.board.delete_board import DeleteBoardUseCase
from app.core.use_cases.v1.board.get_board import GetBoardUseCase

from app.core.dto.board import CreateBoardDto, DeleteBoardDto, GetBoardDto
from app.http.response.presenters.board import GetBoardPresenter, DeleteBoardPresenter


@api.route("/boards", methods=["POST"])
def create_board():
    req = CreateBoardRequestObject.from_dict(a_dict=request.json)

    if not req:
        raise InvalidRequestException(req.get_error_msg(), HTTPStatus.BAD_REQUEST)

    dto = CreateBoardDto(**req.to_dict())

    result = CreateBoardUseCase().execute(dto)

    if not result:
        raise InvalidRequestException(result.type.msg, result.type.code)
    return "done"


@api.route("/boards/<int:board_id>", methods=["DELETE"])
def delete_board(board_id):
    req = DeleteBoardRequestObject.from_dict(a_dict={"board_id": board_id})

    if not req:
        raise InvalidRequestException(req.get_error_msg(), HTTPStatus.BAD_REQUEST)

    dto = DeleteBoardDto(**req.to_dict())

    result = DeleteBoardUseCase().execute(dto)
    if not result:
        raise InvalidRequestException(result.type.msg, result.type.code)
    return DeleteBoardPresenter().transform()


@api.route("/boards", methods=["GET"])
def get_board_list():
    req = GetBoardListRequestObject.from_dict(a_dict=request.args.to_dict())

    if not req:
        raise InvalidRequestException(req.get_error_msg(), HTTPStatus.BAD_REQUEST)

    dto = GetBoardDto(**req.to_dict())

    result = GetBoardUseCase().execute(dto)
    if not result:
        raise InvalidRequestException(result.type.msg, result.type.code)
    return GetBoardPresenter().transform(result)


@api.route("/boards/<int:board_id>", methods=["GET"])
def get_board():
    req = GetBoardListRequestObject.from_dict(a_dict=request.args.to_dict())

    if not req:
        raise InvalidRequestException(req.get_error_msg(), HTTPStatus.BAD_REQUEST)

    dto = GetBoardDto(**req.to_dict())

    result = GetBoardUseCase().execute(dto)
    if not result:
        raise InvalidRequestException(result.type.msg, result.type.code)
    return GetBoardPresenter().transform(result)
