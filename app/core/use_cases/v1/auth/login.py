from typing import Union

from app.core.dto.auth import LoginDto
from app.core.use_cases.base import BaseUseCase

from app.core.use_case_outputs import UseCaseSuccessOutput, UseCaseFailureOutput
from flask_bcrypt import check_password_hash, generate_password_hash


from app.core.exceptions import NotFoundException


class LoginUseCase(BaseUseCase):
    def execute(
        self, dto: LoginDto
    ) -> Union[UseCaseSuccessOutput, UseCaseFailureOutput]:
        result = self.user_repo.get_user(username=dto.username)
        authorized = check_password_hash(result.password, dto.password)
        if not authorized:
            return UseCaseFailureOutput(NotFoundException)
        return UseCaseSuccessOutput(value={"access_token": "temp"})
