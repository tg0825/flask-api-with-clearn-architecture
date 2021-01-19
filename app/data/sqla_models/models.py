from app.extensions.database import db
from app.core.domain.board import Board

# from app.core.domain.user import User


class BoardModels(db.Model):
    __tablename__ = "board"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
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
            is_deleted=self.is_deleted,
        )


class UserModels(db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.Text(), nullable=False)

    def to_entity(self):
        pass
        # return User(id=self.id, username=self.username, password=self.password)
