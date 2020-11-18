from app.repositories import BoardRepository


class BaseUseCase:
    def __init__(
            self,
            board_repo: BoardRepository
    ) -> None:
        self.board_repo = board_repo
        pass
