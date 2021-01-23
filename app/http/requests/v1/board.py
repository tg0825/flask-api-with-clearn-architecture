from typing import Optional, Dict
from voluptuous import (
    Schema,
    Required,
    Optional as VOptional,
    MultipleInvalid,
)

from app.http.requests import InvalidRequestObject


class CreateBoardRequestObject:
    schema = Schema(
        {Required("title"): str, Required("user_id"): int, VOptional("body"): str,}
    )

    def __init__(self, title: str = None, body: str = None, user_id: int = None):
        self.title: str = title
        self.body: str = body
        self.user_id: int = user_id

    @classmethod
    def from_dict(cls, a_dict: Optional[Dict]):
        try:
            cls.schema(a_dict)
            return cls(**a_dict)
        except MultipleInvalid as e:
            return InvalidRequestObject(errors=e.errors, params=a_dict)

    def to_dict(self):
        return dict(title=self.title, body=self.body, user_id=self.user_id)


class DeleteBoardRequestObject:
    schema = Schema({Required("board_id"): int, Required("user_id"): int})

    def __init__(self, board_id: int = None, user_id: int = None):
        self.board_id: int = board_id
        self.user_id: int = user_id

    @classmethod
    def from_dict(cls, a_dict: Optional[Dict[str, int]]):
        try:
            cls.schema(a_dict)
            return cls(**a_dict)
        except MultipleInvalid as e:
            return InvalidRequestObject(errors=e.errors, params=a_dict)

    def to_dict(self):
        return dict(board_id=self.board_id, user_id=self.user_id)


class GetBoardListRequestObject:
    schema = Schema(
        {
            VOptional("search_word"): str,
            VOptional("search_type"): str,
            VOptional("page"): str,
        }
    )

    def __init__(
        self, search_word: str = None, search_type: str = None, page: str = None
    ) -> None:
        self.search_word: str = search_word
        self.search_type: str = search_type
        self.page: str = page

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
        return dict(
            search_word=self.search_word,
            search_type=self.search_type,
            page=int(self.page) if self.page is not None else self.page,
        )
