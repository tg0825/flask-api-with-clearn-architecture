from app.extensions.database import db

class BoardModels(db.Model):
    __tablename__ = 'board'

    id = db.Column()
    title = db.Column()
    user_id = db.Column()
    is_deleted = db.Column()