from app.core.dto.board import CreateBoardDto
from app.core.use_cases.base import BaseUseCase


class CreateBoardUseCase(BaseUseCase):
    def execute(self, dto=CreateBoardDto):
        if not dto.text:
            return

        board = self.board_repo.create_board(dto=dto)
