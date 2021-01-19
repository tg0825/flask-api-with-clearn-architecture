from typing import Optional, Dict
from voluptuous import (
    Schema,
    Required,
    Optional as VOptional,
    MultipleInvalid,
)

from app.http.requests import InvalidRequestObject


class CreateUserRequestObject:
    schema = Schema({Required("username"): str, Required("password"): str,})

    def __init__(
        self, username: str = None, password: str = None,
    ):
        self.username: str = username
        self.password: str = password

    @classmethod
    def from_dict(cls, a_dict: Optional[Dict]):
        try:
            cls.schema(a_dict)
            return cls(**a_dict)
        except MultipleInvalid as e:
            return InvalidRequestObject(errors=e.errors, params=a_dict)

    def to_dict(self):
        return dict(username=self.username, password=self.password)
