from http import HTTPStatus
from flask import jsonify

from app.core.schemas.user import UserResponseSchema
from app.core.use_case_outputs import UseCaseSuccessOutput


class CreateUserPresenter:
    def transform(self, response: UseCaseSuccessOutput) -> jsonify:
        schema = UserResponseSchema()
        status_code = HTTPStatus.CREATED
        result = {"data": {"user": schema.dump(response.value)}}
        return jsonify(**result), status_code
