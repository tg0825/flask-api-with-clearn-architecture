from datetime import timedelta
from typing import Union
from flask_jwt_extended import create_access_token

from app import bcrypt
from app.core.exceptions import NotFoundException
from app.core.dto.auth import LoginDto
from app.core.use_cases.base import BaseUseCase
from app.core.use_case_outputs import UseCaseSuccessOutput, UseCaseFailureOutput


class LoginUseCase(BaseUseCase):
    def execute(
        self, dto: LoginDto
    ) -> Union[UseCaseSuccessOutput, UseCaseFailureOutput]:
        user = self.user_repo.get_user(username=dto.username)
        authorized = bcrypt.check_password_hash(user.password, dto.password)
        if not authorized:
            return UseCaseFailureOutput(NotFoundException)
        expires = timedelta(days=1)
        access_token = create_access_token(identity=str(user.id), expires_delta=expires)
        return UseCaseSuccessOutput(value={"access_token": access_token})
