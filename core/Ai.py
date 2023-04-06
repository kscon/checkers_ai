class Ai:
    color = 0  # white=0, black=1
    method = 'random'

    def get_move(self, board):
        move = ''
        self.enumerate_moves(board)
        self.evaluate_moves()
        return move

    def enumerate_moves(self, board):
        list_of_moves = []  # in the fashion of = ['a3b4', 'c3b5', ...]
        play_direction = 1
        if self.color == 1:
            play_direction = -1

        for col in board.cols:
            for row in board.rows:
                field = board.get_field(col, row)
                if field.get_Piece() is not None:
                    piece = field.get_Piece()
                    if self.color == 0 and piece.player_color == 'white' or \
                            self.color == 1 and piece.player_color == 'black':
                        if piece.get_piece_type() == 'pawn':
                            # enumerate possible moves
                            target_col = chr(ord(col) - 1)
                            target_row = row + play_direction

                            list_of_moves.append(col + str(row) + target_col + str(target_row))
        return list_of_moves

    def evaluate_moves(self):
        pass
