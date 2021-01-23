from dataclasses import dataclass
from datetime import datetime


@dataclass
class User:
    id: int = None
    username: str = None
    password: str = None
    created_at: datetime = None
    updated_at: datetime = None
