from app.core.dto.board import CreateBoardDto


class BoardRepository:
    def create_board(self, dto: CreateBoardDto = None) -> Board:
        board = BoardModels(
            title=dto.title,
            text=dto.text,
            user_id=dto.user_id,
            is_deleted=False
        )

        session.add(board)
        session.commit()
        return board.to_entity()
