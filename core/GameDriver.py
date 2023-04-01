from core.Board import Board


class GameDriver:
    game_board = Board()
    current_player = 0  # white=0, black=1

    def print_board(self):
        print(self.game_board.board_to_string())

    def make_move(self, source_field, target_field):
        try:
            source_col, source_row = source_field
            target_col, target_row = target_field
            source_row = int(source_row)
            target_row = int(target_row)
            assert isinstance(source_col, str) and source_col in self.game_board.cols
            assert isinstance(source_row, int) and source_row in self.game_board.rows
            assert isinstance(target_col, str) and target_col in self.game_board.cols
            assert isinstance(target_row, int) and target_row in self.game_board.rows
        except AssertionError:
            print('Not a valid field/notation!')
            return -1

        res = self.is_valid_move(source_col, source_row, target_col, target_row)
        if res[0] == 1:
            self.game_board.move_piece(source_col, source_row, target_col, target_row)
            if res[1] is not None:
                self.game_board.remove_piece(res[1].col, res[1].row)
            self.current_player = (self.current_player + 1) % 2
        else:
            print('Move ' + source_field + '->' + target_field + ' is not legal!')

    # todo: testing
    # expects valid source and target field (i.e., on the board),
    # validation of the move itself is done here
    # returns: (code, field), where field depicts a checked piece or None, and code
    # -1 for an invalid move
    # 1 for a vaild move
    def is_valid_move(self, source_col, source_row, target_col, target_row):
        piece = self.game_board.get_field(source_col, source_row).get_Piece()
        current_player = self.current_player
        col_index_source = self.game_board.cols.index(source_col)
        row_index_source = self.game_board.rows.index(source_row)
        col_index_target = self.game_board.cols.index(target_col)
        row_index_target = self.game_board.rows.index(target_row)
        checked_field = ' '

        play_direction = 1  # 1 for white, -1 for black
        if self.current_player == 1:
            play_direction = -1

        # pawn moves
        if piece.get_piece_type() == 'pawn':
            # normal moves
            if abs(col_index_source - col_index_target) == 1:
                target_field = self.game_board.get_field(target_col, target_row)
                if target_row - source_row == play_direction and target_field.get_Piece() is None:
                    return 1, None
                """# normal move white
                if target_row - source_row == 1 and current_player == 0 and target_piece is None:
                    return 1
                # normal move black
                elif target_row - source_row == -1 and current_player == 1 and target_piece == ' ':
                    return 1"""

            # checking moves
            elif abs(col_index_source - col_index_target) == 2:
                # checking move left forward
                target_field = self.game_board.get_field(target_col, target_row)
                if target_row - source_row == 2 * play_direction and \
                        target_field.get_Piece() is None:
                    checked_field = self.game_board.get_field_by_index(
                        col_index_source + (col_index_target - col_index_source) - 1,
                        row_index_source + play_direction)
                    if checked_field.get_Piece() is None:
                        return -1, None
                    if checked_field.get_Piece().player_color == 'white' and current_player == 1:
                        return 1, checked_field
                    elif checked_field.get_Piece().player_color == 'black' and current_player == 0:
                        return 1, checked_field
            """# checking move left backwards
                        elif target_row - source_row == -2:
                            checked_piece = self.game_board.get_field(
                                self.game_board.cols[col_index_source + 1], source_row - 1).get_piece()
                            if checked_piece == 'b' or checked_piece == 'B':
                                return True
                        # checking move right
                        elif self.game_board.cols.index(source_col) - self.game_board.cols.index(target_col) == 2:
                            # checking move right forward
                            if target_row - source_row == 2:
                                checked_piece = self.game_board.get_field(
                                    self.game_board.cols[col_index_source - 1], source_row + 1).get_piece()
                                if checked_piece == 'b' or checked_piece == 'B':
                                    return True
                            # checking move right backwards
                            elif target_row - source_row == -2:
                                checked_piece = self.game_board.get_field(
                                    self.game_board.cols[col_index_source - 1], source_row - 1).get_piece()
                                if checked_piece == 'b' or checked_piece == 'B':
                                    return True"""
            # move not valid
        return -1, None


gd = GameDriver()
# gd.print_board()
gd.make_move('a3', 'b4')
gd.print_board()
gd.make_move('b6', 'a5')
gd.print_board()
gd.make_move('c3', 'd4')
gd.print_board()
gd.make_move('a5', 'c3')
gd.print_board()
gd.make_move('b2', 'c3')

# print(gd.is_valid_move('a', 3, 'b', 4))
