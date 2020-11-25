from typing import List


class InvalidRequestObject:
    def __init__(self, errors: List = None, params: dict = None):
        self.errors = errors
        self.params = params
