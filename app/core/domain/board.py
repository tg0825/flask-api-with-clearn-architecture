from dataclasses import dataclass


@dataclass
class Board:
    id: int = None
    title: str = None
    body: str = None
    user_id: int = None
    is_deleted: bool = None

