from typing import List

from app.core.dto.board import CreateBoardDto, DeleteBoardDto, GetBoardListDto
from app.core.enum import BoardSearchTypeEnum, BoardPaginationEnum
from app.data.sqla_models.models import BoardModels, UserModels
from app.core.domain.board import Board

from app.extensions.database import session
from app.core.exceptions import NotFoundException

from sqlalchemy.orm import aliased

from app.extensions.utils.cursor.cursor import Paginate


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
        self, search_type: str = None, search_word: str = None, page: int = None
    ) -> List:
        search_filter = []
        if search_word:
            if search_type == BoardSearchTypeEnum.TITLE:
                search_filter.append(BoardModels.title.ilike(search_word))

            if search_type == BoardSearchTypeEnum.USER_ID:
                search_filter.append(BoardModels.user_id.ilike(search_word))
        board_pagination = (
            session.query(BoardModels)
            .filter(*search_filter)
            .paginate(page=page, per_page=BoardPaginationEnum.BOARD_PAGE)
        )
        return [
            [item.to_entity() for item in board_pagination.items],
            Paginate(
                total=board_pagination.total,
                count=len(board_pagination.items),
                per_page=board_pagination.per_page,
                current_page=board_pagination.page,
                total_pages=board_pagination.pages,
            ),
        ]

    def get_board(self, board_id: int = None) -> Board:
        bm = aliased(BoardModels)
        board = session.query(bm).filter(bm.id == board_id).first()

        if not board:
            raise NotFoundException()
        return board.to_entity()


class UserRepository:
    def create_user(self, username: str = None, password: str = None) -> UserModels:
        user = UserModels(username=username, password=password)
        session.add(user)
        session.commit()
        return user
