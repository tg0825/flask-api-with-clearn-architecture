from dataclasses import dataclass


@dataclass
class CreateUserDto:
    id: int = None
    username: str = None
    password: str = None
