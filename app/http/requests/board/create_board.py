from typing import Optional, Dict
from voluptuous import Schema, All, Length, Required, Optional as VOptional, MultipleInvalid

from app.http.requests import InvalidRequestObject


class CreateBoardRequestObject:
    schema = Schema({
        Required('title'): str,
        VOptional("body"): str,
    })

    def __init__(
            self,
            title: str = None,
            body: str = None,
    ):
        self.title: str = title
        self.body: str = body

    @classmethod
    def from_dict(cls, a_dict: Optional[Dict]):
        try:
            cls.schema(a_dict)
            return cls(**a_dict)
        except MultipleInvalid as e:
            return InvalidRequestObject(errors=e.errors, params=a_dict)

    def to_dict(self):
        return dict(
            title=self.title,
            body=self.body
        )
