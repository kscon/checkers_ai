class Ai:
    color = 0  # white=0, black=1
    method = 'random'

    def get_move(self, board):
        move = ''
        self.enumerate_moves(board)
        self.evaluate_moves()
        return move

    def enumerate_moves(self, board):
        pass

    def evaluate_moves(self):
        pass
