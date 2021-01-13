from typing import Dict


class UseCaseFailureOutput:
    def __init__(self, type: str, message: str = None) -> None:
        self.type = type
        self.message = self._format_message(message if message is not None else type)

    def _format_message(self, msg):
        if isinstance(msg, Exception):
            return msg.__class__.__name__
        return msg

    @property
    def value(self) -> Dict:
        return {"type": self.type, "message": self.message}

    def __bool__(self) -> bool:
        return False


class UseCaseSuccessOutput:
    SUCCESS = "Success"

    def __init__(self, value=None, meta=None):
        self.type = self.SUCCESS
        self.value = value
        self.meta = meta

    # 해당 클래스를 bool로 채크할 경우에 대응하는 메서드
    def __bool__(self):
        return True
