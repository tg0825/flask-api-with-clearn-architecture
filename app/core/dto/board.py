from dataclasses import dataclass


@dataclass
class CreateBoardDto:
    title: str = None
    body: str = None
    user_id: int = None


@dataclass
class EditBoardDto:
    board_id: int = None
    user_id: int = None
    title: str = None
    body: str = None


@dataclass
class DeleteBoardDto:
    board_id: int = None
    user_id: int = None


@dataclass
class GetBoardListDto:
    # 검색 종류: 제목, 내용, 유저 아이디
    search_type: str = None
    search_word: str = None
    page: int = None


@dataclass
class GetBoardDto:
    board_id: int = None
