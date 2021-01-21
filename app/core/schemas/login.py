from marshmallow import fields

from app.core.schemas import BaseSchema


class LoginResponseSchema(BaseSchema):
    access_token = fields.String(required=True)
