from typing import List

from app.core.dto.board import CreateBoardDto, DeleteBoardDto, GetBoardDto
from app.data.sqla_models.models import BoardModels
from app.core.domain.board import Board

from app.extensions.database import session


class BoardRepository:
    def create_board(self, dto: CreateBoardDto = None) -> Board:
        board = BoardModels(
            title=dto.title, body=dto.body, user_id=dto.user_id, is_deleted=False
        )

        session.add(board)
        session.commit()
        return board.to_entity()

    def delete_board(self, dto: DeleteBoardDto = None) -> None:
        session.query(BoardModels).filter(BoardModels.id == dto.id).delete(BoardModels)
        session.commit()

    def get_board(self, dto: GetBoardDto = None) -> List[Board]:
        board = session.query(BoardModels).all()
        return [item.to_entity() for item in board]
