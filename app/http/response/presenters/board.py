from http import HTTPStatus
from flask import jsonify

from app.core.use_case_outputs import UseCaseSuccessOutput


class GetBoardPresenter:
    def transform(self, response: UseCaseSuccessOutput):
        schema = BoardResponseSchema()
        status_code = HTTPStatus.OK
        result = {
            "data": {"boards": schema.dump().data},
            # TODO :: 추후 처리
            # "meta": {
            #
            # }
        }
        return jsonify(**result), status_code
