from flask import request
from http import HTTPStatus

from app.core.dto.auth import LoginDto
from app.core.use_cases.v1.auth.login import LoginUseCase
from app.http.api import api, InvalidRequestException
from app.http.requests.v1.auth import LoginRequestObject
from app.http.response.presenters.auth import LoginPresenter


@api.route("/v1/login", methods=["POST"])
def login():
    req = LoginRequestObject.from_dict(a_dict=request.json)

    if not req:
        raise InvalidRequestException(req.get_error_msg(), HTTPStatus.BAD_REQUEST)

    dto = LoginDto(**req.to_dict())
    result = LoginUseCase().execute(dto)

    if not result:
        raise InvalidRequestException(result.type.msg, result.type.code)

    return LoginPresenter().transform(response=result)
