from app.extensions.database import db
from app.core.domain.board import Board


class BoardModels(db.Model):
    __tablename__ = 'board'

    id = db.Column(
        primary_key=True
    )
    title = db.Column()
    body = db.Column()
    user_id = db.Column()
    is_deleted = db.Column()

    def to_entity(self):
        return Board(
            id=self.id,
            title=self.title,
            body=self.body,
            user_id=self.user_id,
            is_deleted=self.is_deleted
        )