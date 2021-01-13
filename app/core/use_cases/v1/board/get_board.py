from typing import Union

from app.core.dto.board import GetBoardDto
from app.core.use_cases.base import BaseUseCase

from app.core.use_case_outputs import UseCaseSuccessOutput, UseCaseFailureOutput

from app.core.exceptions import NotFoundException


class GetBoardUseCase(BaseUseCase):
    def execute(
        self, dto: GetBoardDto
    ) -> Union[UseCaseSuccessOutput, UseCaseFailureOutput]:
        try:
            board = self.board_repo.get_board(board_id=dto.board_id)
        except NotFoundException as e:
            return UseCaseFailureOutput(e)

        return UseCaseSuccessOutput(value=board)
