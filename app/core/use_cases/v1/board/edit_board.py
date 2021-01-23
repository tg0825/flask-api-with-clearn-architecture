from typing import Union

from app.core.domain.board import Board
from app.core.dto.board import EditBoardDto
from app.core.use_cases.base import BaseUseCase

from app.core.use_case_outputs import UseCaseSuccessOutput, UseCaseFailureOutput

from app.core.exceptions import NotFoundException


class EditBoardUseCase(BaseUseCase):
    def execute(
        self, dto: EditBoardDto
    ) -> Union[UseCaseSuccessOutput, UseCaseFailureOutput]:
        try:
            board: Board = self.board_repo.get_board(board_id=dto.board_id)

            if board.user_id != dto.user_id:
                return UseCaseFailureOutput(NotFoundException())

            board: Board = self.board_repo.edit_board(dto=dto)

            return UseCaseSuccessOutput(value=board)
        except NotFoundException:
            return UseCaseFailureOutput(NotFoundException())
