import Board


class Gamedriver:
    game_board = board.Board()
    # current_player = 0  # white=0, black=1

    """def print_board(self):
        print(self.game_board.board_to_string())"""

    def make_move(self, source_field, target_field):
        try:
            source_col, source_row = source_field
            target_col, target_row = target_field
            assert isinstance(source_col, str) and source_col in self.game_board.cols
            assert isinstance(source_row, int) and source_row in self.game_board.rows
            assert isinstance(target_col, str) and target_col in self.game_board.cols
            assert isinstance(target_row, int) and target_row in self.game_board.rows
        except:
            print('Not a valid notation!')
            return -1

        if self.is_valid_move(source_col, source_row, target_col, target_row):
            pass

    def is_valid_move(self, source_col, source_row, target_col, target_row):
        piece = self.game_board.get_field(source_col, source_row)

        if self.current_player == 0:
            if piece == 'w' or piece == 'W':
                pass
