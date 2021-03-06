from flask import request
from http import HTTPStatus
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.core.exceptions import InvalidRequestException
from app.core.use_cases.v1.board.edit_board import EditBoardUseCase

from app.http.api import api
from app.http.requests.v1.board import (
    CreateBoardRequestObject,
    DeleteBoardRequestObject,
    GetBoardListRequestObject,
    EditBoardRequestObject,
)

from app.core.use_cases.v1.board.create_board import CreateBoardUseCase
from app.core.use_cases.v1.board.delete_board import DeleteBoardUseCase
from app.core.use_cases.v1.board.get_board_list import GetBoardListUseCase
from app.core.use_cases.v1.board.get_board import GetBoardUseCase

from app.core.dto.board import (
    CreateBoardDto,
    DeleteBoardDto,
    GetBoardListDto,
    GetBoardDto,
    EditBoardDto,
)
from app.http.response.presenters.board import (
    GetBoardListPresenter,
    DeleteBoardPresenter,
    GetBoardPresenter,
    CreateBoardPresenter,
    EditBoardPresenter,
)


@api.route("/v1/boards", methods=["POST"])
@jwt_required
def create_board():
    user_id = get_jwt_identity()
    req = CreateBoardRequestObject.from_dict(
        a_dict={"user_id": int(user_id), **request.json}
    )

    if not req:
        raise InvalidRequestException(req.get_error_msg(), HTTPStatus.BAD_REQUEST)

    dto = CreateBoardDto(**req.to_dict())

    result = CreateBoardUseCase().execute(dto)

    if not result:
        raise InvalidRequestException(result.type.msg, result.type.code)
    return CreateBoardPresenter().transform(response=result)


@api.route("/v1/boards/<int:board_id>", methods=["PATCH"])
@jwt_required
def edit_board(board_id: int):
    user_id = get_jwt_identity()
    req = EditBoardRequestObject.from_dict(
        a_dict={"user_id": int(user_id), "board_id": board_id, **request.json}
    )

    if not req:
        raise InvalidRequestException(req.get_error_msg(), HTTPStatus.BAD_REQUEST)

    dto = EditBoardDto(**req.to_dict())

    result = EditBoardUseCase().execute(dto)

    if not result:
        raise InvalidRequestException(result.type.msg, result.type.code)
    return EditBoardPresenter().transform(response=result)


@api.route("/v1/boards/<int:board_id>", methods=["DELETE"])
@jwt_required
def delete_board(board_id: int):
    user_id = get_jwt_identity()
    req = DeleteBoardRequestObject.from_dict(
        a_dict={"board_id": board_id, "user_id": int(user_id)}
    )

    if not req:
        raise InvalidRequestException(req.get_error_msg(), HTTPStatus.BAD_REQUEST)

    dto = DeleteBoardDto(**req.to_dict())

    result = DeleteBoardUseCase().execute(dto)
    if not result:
        raise InvalidRequestException(result.type.msg, result.type.code)
    return DeleteBoardPresenter().transform()


@api.route("/v1/boards", methods=["GET"])
def get_board_list():
    req = GetBoardListRequestObject.from_dict(a_dict=request.args.to_dict())

    if not req:
        raise InvalidRequestException(req.get_error_msg(), HTTPStatus.BAD_REQUEST)

    dto = GetBoardListDto(**req.to_dict())

    result = GetBoardListUseCase().execute(dto=dto)
    if not result:
        raise InvalidRequestException(result.type.msg, result.type.code)
    return GetBoardListPresenter().transform(result)


@api.route("/v1/boards/<int:board_id>", methods=["GET"])
def get_board(board_id: int):
    dto = GetBoardDto(board_id=board_id)

    result = GetBoardUseCase().execute(dto=dto)
    if not result:
        raise InvalidRequestException(result.type.msg, result.type.code)
    return GetBoardPresenter().transform(result)
