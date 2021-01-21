from datetime import datetime, timedelta
from typing import Union

from app.core.dto.auth import LoginDto
from app.core.use_cases.base import BaseUseCase

from app.core.use_case_outputs import UseCaseSuccessOutput, UseCaseFailureOutput
from flask_bcrypt import check_password_hash, generate_password_hash
from flask_jwt_extended import create_access_token


from app.core.exceptions import NotFoundException


class LoginUseCase(BaseUseCase):
    def execute(
        self, dto: LoginDto
    ) -> Union[UseCaseSuccessOutput, UseCaseFailureOutput]:
        user = self.user_repo.get_user(username=dto.username)
        authorized = check_password_hash(user.password, dto.password)
        if not authorized:
            return UseCaseFailureOutput(NotFoundException)
        expires = timedelta(days=1)
        access_token = create_access_token(identity=str(user.id), expires_delta=expires)
        return UseCaseSuccessOutput(value={"access_token": access_token})
