from typing import Optional, Dict
from voluptuous import (
    Schema,
    Required,
    Optional as VOptional,
    MultipleInvalid,
)

from app.http.requests import InvalidRequestObject


class CreateBoardRequestObject:
    schema = Schema({Required("title"): str, VOptional("body"): str,})

    def __init__(
        self, title: str = None, body: str = None,
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
        return dict(title=self.title, body=self.body)


class DeleteBoardRequestObject:
    schema = Schema({Required("board_id"): int})

    def __init__(self, board_id: int = None):
        self.board_id: int = board_id

    @classmethod
    def from_dict(cls, a_dict: Optional[Dict[str, int]]):
        try:
            cls.schema(a_dict)
            return cls(**a_dict)
        except MultipleInvalid as e:
            return InvalidRequestObject(errors=e.errors, params=a_dict)

    def to_dict(self):
        return dict(board_id=self.board_id)


class GetBoardRequestObject:
    schema = Schema({VOptional("search_word"): str, VOptional("search_type"): str})

    def __init__(self, search_word: str = None, search_type: str = None):
        self.search_word: str = search_word
        self.search_type: str = search_type

    @classmethod
    def from_dict(cls, a_dict: Optional[Dict] = {}):
        try:
            # 유효성 검사 이상 있을 경우 raise
            cls.schema(a_dict)
            # 유효성 검사 이상 없을 시 인스턴스 생성
            return cls(**a_dict)
        except MultipleInvalid as e:
            return InvalidRequestObject(errors=e.errors, params=a_dict)

    def to_dict(self):
        return dict(search_word=self.search_word, search_type=self.search_type)
