from app.core.dto.board import CreateBoardDto
from app.data.sqla_models.models import BoardModels
from app.core.domain.board import Board


class BoardRepository:
    def create_board(self, dto: CreateBoardDto = None) -> Board:
        board = BoardModels(
            title=dto.title,
            text=dto.text,
            body=dto.body,
            user_id=dto.user_id,
            is_deleted=False
        )

        session.add(board)
        session.commit()
        return board.to_entity()
