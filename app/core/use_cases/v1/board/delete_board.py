from typing import Union

from app.core.dto.board import DeleteBoardDto
from app.core.use_cases.base import BaseUseCase

from app.core.use_case_outputs import UseCaseSuccessOutput, UseCaseFailureOutput

from app.core.exceptions import NotFoundException, NoAuthorizationControlException


class DeleteBoardUseCase(BaseUseCase):
    def execute(
        self, dto: DeleteBoardDto
    ) -> Union[UseCaseSuccessOutput, UseCaseFailureOutput]:
        # 글 존재 여부 채크
        try:
            board = self.board_repo.get_board(dto.id)
        except NotFoundException as e:
            return UseCaseFailureOutput(e)

        # 본인 글 여부 채크
        if board.user_id != dto.user_id:
            # TODO :: excption 인증여부 실패
            return UseCaseFailureOutput(NoAuthorizationControlException)

        self.board_repo.delete_board(dto=dto)

        return UseCaseSuccessOutput()
