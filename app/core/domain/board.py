from dataclasses import dataclass
from datetime import datetime


@dataclass
class Board:
    id: int = None
    title: str = None
    body: str = None
    user_id: int = None
    is_deleted: bool = None
    created_at: datetime = None
    updated_at: datetime = None
