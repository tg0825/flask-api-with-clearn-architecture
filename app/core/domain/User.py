from dataclasses import dataclass


@dataclass
class User:
    id: int = None
    username: str = None
    password: str = None
