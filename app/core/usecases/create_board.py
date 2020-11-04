from app.core.dto.board import CreateBoardDto
from app.core.usecases.base import BaseUseCase


class CreateBoardUseCase(BaseUseCase):
    def execute(self, dto=CreateBoardDto):
        if not dto.body:
            return

        board = self.board_repo.create_board(dto=dto)
