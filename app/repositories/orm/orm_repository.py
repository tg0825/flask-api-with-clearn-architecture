from typing import List

from app.core.dto.board import CreateBoardDto, DeleteBoardDto, GetBoardListDto
from app.core.enum import BoardSearchTypeEnum
from app.data.sqla_models.models import BoardModels
from app.core.domain.board import Board

from app.extensions.database import session
from app.core.exceptions import NotFoundException

from sqlalchemy.orm import aliased


class BoardRepository:
    def create_board(self, dto: CreateBoardDto = None) -> Board:
        board = BoardModels(
            title=dto.title, body=dto.body, user_id=dto.user_id, is_deleted=False
        )

        session.add(board)
        session.commit()
        return board.to_entity()

    def delete_board(self, dto: DeleteBoardDto = None) -> None:
        session.query(BoardModels).filter(BoardModels.id == dto.board_id).delete()
        session.commit()

    def get_board_list(
        self, search_type: str = None, search_word: str = None
    ) -> List[Board]:
        search_filter = []
        if search_word:
            if search_type == BoardSearchTypeEnum.TITLE:
                search_filter.append(BoardModels.title.ilike(search_word))

            if search_type == BoardSearchTypeEnum.USER_ID:
                search_filter.append(BoardModels.user_id.ilike(search_word))
        board = session.query(BoardModels).filter(*search_filter).all()
        print(board)
        return [item.to_entity() for item in board]

    def get_board(self, board_id: int = None) -> Board:
        bm = aliased(BoardModels)
        board = session.query(bm).filter(bm.id == board_id).first()

        if not board:
            raise NotFoundException()
        return board.to_entity()
