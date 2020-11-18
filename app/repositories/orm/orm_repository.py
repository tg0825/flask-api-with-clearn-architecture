class BoardRepository:
    def create_board(self, dto: CreateDto = None) -> Board:
        board = BoardModles(

        )

        session.add(board)
        session.commit()
        return board.to_entity()
