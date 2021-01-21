from http import HTTPStatus
from flask import jsonify

from app.core.schemas.login import LoginResponseSchema
from app.core.use_case_outputs import UseCaseSuccessOutput


class LoginPresenter:
    def transform(self, response: UseCaseSuccessOutput) -> jsonify:
        schema = LoginResponseSchema()
        status_code = HTTPStatus.ACCEPTED
        result = {"data": schema.dump(response.value)}
        return jsonify(**result), status_code
