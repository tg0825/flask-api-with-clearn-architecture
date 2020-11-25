from typing import Dict


class UseCaseFailerOutput:
    def __init__(self, type: str, message: str = None) -> None:
        self.type = type
        self.message = self._format_message(message if message is not None else type)

    def _format_message(self, msg):
        if isinstance(msg, Exception):
            return msg.__class__.__name__
        return msg

    @property
    def value(self) -> Dict:
        return {
            "type": self.type,
            "message": self.message
        }

    def __bool__(self) -> bool:
        return False
