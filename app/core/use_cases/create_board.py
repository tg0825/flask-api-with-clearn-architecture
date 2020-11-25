from typing import Union

from app.core.dto.board import CreateBoardDto
from app.core.use_cases.base import BaseUseCase

from app.core.use_case_outputs import UseCaseSuccessOutput, UseCaseFailureOutput


class CreateBoardUseCase(BaseUseCase):
    def execute(
            self,
            dto: CreateBoardDto
    ) -> Union[UseCaseSuccessOutput, UseCaseFailureOutput]:
        # if not dto.title:
        #     return

        board = self.board_repo.create_board(dto=dto)
