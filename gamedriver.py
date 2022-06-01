import board

class Gamedriver:
    gameboard = board.Board()
    current_player = 0 # white=0, black=1

    def print_board(self):
        print(self.gameboard.board_to_string())

    def make_move(self,source_field, target_field):
        try:
            assert len(source_field) == 2
            assert len(target_field) == 2
        except:
            print('Not a valid notation!')
            return -1

        source_col, source_row = source_field
        target_col, target_row = target_field

        try:
            source_col.upper()
            target_col.upper()

            valid_cols = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
            valid_rows = range(8)
            assert source_col in valid_cols
            assert target_col in valid_cols
            assert source_row in valid_rows
            assert target_row in valid_rows
        except:
            print('Field is not on the board!')
            return -1

        if is_valid_move()
        ...

    def is_valid_move(self, source_row, source_col, target_row, target_col):
        piece = self.gameboard.get_field_by_notation(source_col, source_row)

        if self.current_player ==0:
            if piece == 'w' or piece == 'W':

