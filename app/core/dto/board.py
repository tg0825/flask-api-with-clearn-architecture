from dataclasses import dataclass

@dataclass
class CreateBoardDto:
    text: str = None
    title: str = None
    user_id: int = None