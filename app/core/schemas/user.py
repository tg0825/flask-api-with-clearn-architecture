from marshmallow import fields

from app.core.schemas import BaseSchema


class UserResponseSchema(BaseSchema):
    id = fields.String(required=True)
    username = fields.String(required=True)
    created_at = fields.String(required=True)
