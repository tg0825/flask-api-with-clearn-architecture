from typing import Optional, Dict
from voluptuous import Schema, All, Length, Required, MultipleInvalid

from app.http.requests import InvalidRequestObject

class CreateBoardRequestObject:
    schema = Schema({
        Required('body'): All(str, Length(max=3000))
    })

    def __init__(self, body: str = None):
        self.body:str = body
        pass

    @classmethod
    def from_dict(cls, a_dict: Optional[Dict]):
        try:
            cls.schema(a_dict)
            return cls(**a_dict)
        except MultipleInvalid as e:
            return InvalidRequestObject(errors=e.errors, params=a_dict)
