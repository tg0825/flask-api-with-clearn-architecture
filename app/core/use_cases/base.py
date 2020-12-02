from app.repositories import BoardRepository

import inject


class BaseUseCase:
    @inject.autoparams()
    def __init__(
            self,
            board_repo: BoardRepository
    ) -> None:
        self.board_repo = board_repo
        pass
