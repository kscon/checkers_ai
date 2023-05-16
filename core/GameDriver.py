from core.Board import Board
from core.Ai import Ai
import random


class GameDriver:
    game_board = Board()
    game_over = 0  # 0 as long as game is going on, 1 if finished
    human_player_color = None
    ai = None

    def __init__(self, human_player_color=None, players=[]):
        self.human_player_color = human_player_color

    def game_loop(self):
        self.prepare_game()
        while not self.game_over:
            self.check_upgrade_condition()
            self.check_winning_condition()
            if self.human_player_color == self.game_board.current_player:
                self.print_board()
                player_move = input('make a move in the form \'a3b4\'...')
                while self.game_board.make_move(self.human_player_color, player_move[:2], player_move[2:]) == -1:
                    player_move = input('try again...')
            else:
                ai_move = self.ai.get_move(self.game_board)
                print('\nAi plays ' + ai_move)
                self.game_board.make_move(self.ai.color, ai_move[:2], ai_move[2:])

    def prepare_game(self):
        if self.human_player_color is None:
            print('Play checkers against the AI!')
            if random.random() > 0.5:
                self.human_player_color = 1
                print('you play the black pieces')
            else:
                print('you play the white pieces')
                self.human_player_color = 0
        self.ai = Ai(color=(self.human_player_color + 1) % 2, game_board=self.game_board)

    def print_board(self):
        print(self.game_board.board_to_string())

    def check_winning_condition(self):
        pass  # todo

    def check_upgrade_condition(self):
        row_color_zipped = [(1,'black'), (8, 'white')]
        for (row, color) in row_color_zipped:
            for col in self.game_board.cols:
                field = self.game_board.get_field(col, row)
                if field.get_Piece() is not None:
                    piece = field.get_Piece()
                    if piece.get_piece_type() == 'pawn' and piece.player_color == color:
                        piece.upgrade_piece()


# gd = GameDriver()
# gd.game_loop()
# gd.print_board()
"""gd.make_move('a3', 'b4')
gd.print_board()
gd.make_move('b6', 'a5')
gd.print_board()
gd.make_move('c3', 'd4')
gd.print_board()
gd.make_move('a5', 'c3')
gd.print_board()
gd.make_move('b2', 'c3')"""

# print(gd.is_valid_move('a', 3, 'b', 4))
