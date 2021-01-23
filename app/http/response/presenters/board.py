from http import HTTPStatus
from flask import jsonify

from app.core.schemas.board import BoardResponseSchema
from app.core.use_case_outputs import UseCaseSuccessOutput


class CreateBoardPresenter:
    def transform(self, response: UseCaseSuccessOutput) -> jsonify:
        schema = BoardResponseSchema()
        status_code = HTTPStatus.CREATED
        result = {"data": {"boards": schema.dump(response.value)}}
        return jsonify(**result), status_code


class GetBoardListPresenter:
    def transform(self, response: UseCaseSuccessOutput) -> jsonify:
        schema = BoardResponseSchema()
        status_code = HTTPStatus.OK
        result = {
            "data": {"boards": schema.dump(response.value, many=True)},
            "meta": response.meta,
        }
        return jsonify(**result), status_code


class GetBoardPresenter:
    def transform(self, response: UseCaseSuccessOutput) -> jsonify:
        schema = BoardResponseSchema()
        status_code = HTTPStatus.OK
        result = {
            "data": {"boards": schema.dump(response.value)},
        }
        return jsonify(**result), status_code


class EditBoardPresenter:
    def transform(self, response: UseCaseSuccessOutput) -> jsonify:
        schema = BoardResponseSchema()
        status_code = HTTPStatus.CREATED
        result = {"data": {"boards": schema.dump(response.value)}}
        return jsonify(**result), status_code


class DeleteBoardPresenter:
    def transform(self) -> jsonify:
        status_code = HTTPStatus.OK
        result = {"data": {"status": True}}
        return jsonify(**result), status_code
