from ctypes import Union

from flask import request
from http import HTTPStatus

from app.core.dto.join import CreateUserDto
from app.core.use_case_outputs import UseCaseSuccessOutput, UseCaseFailureOutput
from app.core.use_cases.v1.join.create_user import CreateUserUseCase
from app.http.api import api, InvalidRequestException
from app.http.requests.v1.join import CreateUserRequestObject
from app.http.response.presenters.join import CreateUserPresenter


@api.route("/v1/join", methods=["POST"])
def join():
    req = CreateUserRequestObject.from_dict(a_dict=request.json)

    if not req:
        raise InvalidRequestException(req.get_error_msg(), HTTPStatus.BAD_REQUEST)

    dto = CreateUserDto(**req.to_dict())
    result = CreateUserUseCase().execute(dto)

    if not result:
        raise InvalidRequestException(result.type.msg, result.type.code)
    return CreateUserPresenter().transform(response=result)
