from core.Board import Board
from core.Ai import Ai
import random


class GameDriver:
    game_board = Board()
    game_over = 0  # 0 as long as game is going on, 1 if finished
    players = {}  # name = player color, .type = human | Ai, .ref = Ai() | None

    # player1 = None
    # player2 = None
    # player1_color = None
    # player2_color = None

    def __init__(self, human_player_color=None, players=[]):
        self.player1_color = human_player_color

    def game_loop(self):
        self.prepare_game()
        while not self.game_over:
            self.check_upgrade_condition()
            self.check_winning_condition()

            for p in self.players:
                if p == self.game_board.current_player:
                    self.print_board()
                    if self.players[p]['type'] == 'human':
                        player_move = input('make a move in the form \'a3b4\'...')
                        while self.game_board.make_move(p, player_move[:2], player_move[2:]) == -1:
                            player_move = input('try again...')
                    elif self.players[p]['type'] == 'Ai':
                        ai_move = self.players[p]['ref'].get_move(self.game_board)
                        print('\nAi plays ' + ai_move)
                        self.game_board.make_move(p, ai_move[:2], ai_move[2:])

    def prepare_game(self):
        while True:
            try:
                game_mode = int(input('State which kind of game you want: '
                                      '\n human vs Ai: 0\n Ai vs Ai: 1\n human vs. human: 2\n'))
                if game_mode in [0, 1, 2]:
                    break
                else:
                    print('try again')
            except:
                print('try again')

        if game_mode == 0:
            print('Play checkers against the AI!')
            coinflip = random.random()
            if coinflip > 0.5:
                print('you play the black pieces')
                player_color = 1
            else:
                print('you play the white pieces')
                player_color = 0
            self.players[player_color] = {'type': 'human', 'ref': None}
            self.players[(player_color + 1) % 2] = \
                {'type': 'Ai', 'ref': Ai(color=(player_color + 1) % 2, game_board=self.game_board)}
            """self.player1_color = 0
            self.player2_color = Ai(color=(self.player1_color + 1) % 2, game_board=self.game_board)"""
        elif game_mode == 1:
            print('An Ai game!')
            self.players[0] = {'type': 'Ai', 'ref': Ai(color=0, game_board=self.game_board)}
            self.players[1] = {'type': 'Ai', 'ref': Ai(color=1, game_board=self.game_board)}
            """player1 = 'Ai'
            player2 = 'Ai'
            self.player1_color = Ai(color=1, game_board=self.game_board)
            self.player2_color = Ai(color=2, game_board=self.game_board)"""
        elif game_mode == 2:
            print('It is a human only game!')
            """player1 = 'human'
            player2 = 'human'
            self.player1_color = 0
            self.player2_color = 1"""
            self.players[0] = {'type': 'human', 'ref': None}
            self.players[1] = {'type': 'human', 'ref': None}

    def print_board(self):
        print(self.game_board.board_to_string())

    def check_winning_condition(self):
        pass  # todo

    def check_upgrade_condition(self):
        row_color_zipped = [(1, 'black'), (8, 'white')]
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
