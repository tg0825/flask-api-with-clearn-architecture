from http import HTTPStatus


class InvalidRequestException(Exception):
    status_code = 400

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv["detail"] = self.message
        return rv


class NotFoundException(Exception):
    code = HTTPStatus.NOT_FOUND
    msg = "not_found"
    pass


class NoAuthorizationControlException(Exception):
    code = HTTPStatus.FORBIDDEN
    msg = "has_not_authorization_to_control"
    pass
