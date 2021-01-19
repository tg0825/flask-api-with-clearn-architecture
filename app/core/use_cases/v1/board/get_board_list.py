from typing import Union, List

from app.core.dto.board import GetBoardListDto
from app.core.use_cases.base import BaseUseCase
from app.core.domain.board import Board

from app.core.use_case_outputs import UseCaseSuccessOutput, UseCaseFailureOutput

from app.core.exceptions import NotFoundException, NoAuthorizationControlException


class GetBoardListUseCase(BaseUseCase):
    def execute(
        self, dto: GetBoardListDto
    ) -> Union[UseCaseSuccessOutput, UseCaseFailureOutput]:
        try:
            boards: List = self.board_repo.get_board_list(
                search_type=dto.search_type, search_word=dto.search_word, page=dto.page
            )
        except NotFoundException as e:
            return UseCaseFailureOutput(e)

        return UseCaseSuccessOutput(value=boards[0], meta=boards[1])
