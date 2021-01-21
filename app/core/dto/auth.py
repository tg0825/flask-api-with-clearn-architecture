from dataclasses import dataclass


@dataclass
class LoginDto:
    username: str = None
    password: str = None
