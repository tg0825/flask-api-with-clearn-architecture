from http import HTTPStatus
from flask import jsonify

from app.core.schemas.board import BoardResponseSchema
from app.core.use_case_outputs import UseCaseSuccessOutput


class GetBoardPresenter:
    def transform(self, response: UseCaseSuccessOutput) -> jsonify:
        schema = BoardResponseSchema()
        status_code = HTTPStatus.OK
        result = {
            "data": {"boards": schema.dump(response.value, many=True)},
            "meta": {},
        }
        return jsonify(**result), status_code
