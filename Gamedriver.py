import board


class Gamedriver:
    gameboard = board.Board()
    current_player = 0  # white=0, black=1

    def print_board(self):
        print(self.gameboard.board_to_string())

    def make_move(self, source_field, target_field):
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

        if is_valid_move():
            pass

    # expects valid source and target field (i.e., on the board), rest is done here
    def is_valid_move(self, source_row, source_col, target_row, target_col):
        piece = self.gameboard.get_field(source_col, source_row).get_Piece()
        current_player = self.current_player
        col_index_source = self.gameboard.cols.index(source_col)
        col_index_target = self.gameboard.cols.index(target_col)
        checked_piece = ' '

        # todo
        # normal moves
        # normal move left and right
        if abs(col_index_source - col_index_target) == 1:
            # normal move forward
            if target_row - source_row == 1:
                target_piece = self.gameboard.get_field(target_col, target_row)
                if current_player == 0 and target_piece == ' ' or \
                        current_player == 1 and piece == 'B':
                    return 1
            # normal move backwards
            if target_row - source_row == -1:
                target_piece = self.gameboard.get_field(target_col, target_row)
                if current_player == 1 and target_piece == ' ' or \
                        current_player == 0 and piece == 'W':
                    return 1
        # checking moves
        # checking move left
        elif self.gameboard.cols.index(source_col) - self.gameboard.cols.index(target_col) == -2:
            # checking move left forward
            if target_row - source_row == 2:
                checked_piece=self.gameboard.get_field(
                    self.gameboard.cols[col_index_source+1],source_row+1).get_piece()
                if checked_piece == 'b' or checked_piece == 'B':
                    return True
            # checking move left backwards
            elif target_row - source_row == -2:
                checked_piece=self.gameboard.get_field(
                    self.gameboard.cols[col_index_source+1],source_row-1).get_piece()
                if checked_piece == 'b' or checked_piece == 'B':
                    return True
        # checking move right
        elif self.gameboard.cols.index(source_col) - self.gameboard.cols.index(target_col) == 2:
            # checking move right forward
            if target_row - source_row == 2:
                checked_piece=self.gameboard.get_field(
                    self.gameboard.cols[col_index_source-1],source_row+1).get_piece()
                if checked_piece == 'b' or checked_piece == 'B':
                    return True
            # checking move right backwards
            elif target_row - source_row == -2:
                checked_piece=self.gameboard.get_field(
                    self.gameboard.cols[col_index_source-1],source_row-1).get_piece()
                if checked_piece == 'b' or checked_piece == 'B':
                    return True
