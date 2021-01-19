from app.repositories import BoardRepository, UserRepository

import inject


class BaseUseCase:
    @inject.autoparams()
    def __init__(self, board_repo: BoardRepository, user_repo: UserRepository) -> None:
        self.board_repo = board_repo
        self.user_repo = user_repo
        pass
