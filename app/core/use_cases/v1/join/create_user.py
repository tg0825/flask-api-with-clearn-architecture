from typing import Union

from app.core.dto.join import CreateUserDto
from app.core.use_cases.base import BaseUseCase

from app.core.use_case_outputs import UseCaseSuccessOutput, UseCaseFailureOutput

from app.core.exceptions import NotFoundException


class CreateUserUseCase(BaseUseCase):
    def execute(
        self, dto: CreateUserDto
    ) -> Union[UseCaseSuccessOutput, UseCaseFailureOutput]:
        # if not dto.user_id:
        #     return UseCaseFailureOutput(NotFoundException())

        result = self.user_repo.create_user(
            username=dto.username, password=dto.password
        )

        return UseCaseSuccessOutput(value=result)
