from marshmallow import fields

from app.core.schemas import BaseSchema


class BoardResponseSchema(BaseSchema):
    id = fields.String(required=True)
    title = fields.String(required=True)
    user_id = fields.String(required=True)
    is_deleted = fields.Boolean(required=True)
    body = fields.String(required=True)
    created_at = fields.String(required=True)
    updated_at = fields.String(required=True)
