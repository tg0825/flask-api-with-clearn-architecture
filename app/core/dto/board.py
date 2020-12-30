from dataclasses import dataclass


@dataclass
class CreateBoardDto:
    title: str = None
    body: str = None
    user_id: int = None


@dataclass
class DeleteBoardDto:
    board_id: int = None


@dataclass
class GetBoardDto:
    search_word: str = None
    search_type: str = None