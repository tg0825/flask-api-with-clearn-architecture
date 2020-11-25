from http import HTTPStatus


class InvalidRequestException(Exception):
    status_code = 400


class NotFoundException(Exception):
    code = HTTPStatus.NOT_FOUND
    msg = "not_found"
    pass
