from core.Board import Board
from core.Ai import Ai
import random
import copy


class GameDriver:
    game_board = Board()
    moves = 0
    # game_over = 0  # 0 as long as game is going on, 1 if finished
    players = {}  # name = player color, .type = human | Ai, .ref = Ai() | None
    ai_depth = 5
    # player1 = None
    # player2 = None
    # player1_color = None
    # player2_color = None

    def __init__(self, human_player_color=None, players=[]):
        self.player1_color = human_player_color

    def game_loop(self):
        self.prepare_game()
        while True:
            self.print_board()
            self.check_upgrade_condition()
            if self.check_winning_condition():
                print('Game ended after ' + str(self.moves) + ' moves.')
                print('GAME OVER!')
                break

            for p in self.players:
                if p == self.game_board.current_player:
                    if self.players[p]['type'] == 'human':
                        player_move = input('make a move in the form \'a3b4\'...')
                        while self.game_board.make_move(p, player_move[:2], player_move[2:]) == -1:
                            player_move = input('try again...')
                    elif self.players[p]['type'] == 'Ai':
                        ai_move = self.players[p]['ref'].get_move(copy.deepcopy(self.game_board))
                        print('\nAi plays ' + ai_move)
                        self.game_board.make_move(p, ai_move[:2], ai_move[2:])
                    break
            self.moves +=1

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
                {'type': 'Ai', 'ref': Ai(color=(player_color + 1) % 2, game_board=copy.deepcopy(self.game_board), depth=self.ai_depth)}
        elif game_mode == 1:
            print('An Ai game!')
            self.players[0] = {'type': 'Ai', 'ref': Ai(color=0, game_board=copy.deepcopy(self.game_board), depth=self.ai_depth)}
            self.players[1] = {'type': 'Ai', 'ref': Ai(color=1, game_board=copy.deepcopy(self.game_board), depth=self.ai_depth)}
        elif game_mode == 2:
            print('It is a human only game!')
            self.players[0] = {'type': 'human', 'ref': None}
            self.players[1] = {'type': 'human', 'ref': None}

    def print_board(self):
        print(self.game_board.board_to_string())

    def check_winning_condition(self):
        player0_flag = False
        player1_flag = False
        for col in self.game_board.cols:
            for row in self.game_board.rows:
                field = self.game_board.get_field(col, row)
                if field.get_Piece() is not None:
                    piece = field.get_Piece()
                    if piece.player_color == 'white':
                        player0_flag = True
                    elif piece.player_color == 'black':
                        player1_flag = True
                if player0_flag and player1_flag:
                    return False
        if not player0_flag:
            print('player 1 wins!')
        elif not player1_flag:
            print('player 0 wins!')
        elif not player1_flag and not player1_flag:
            assert False
        return True

    def check_upgrade_condition(self):
        row_color_zipped = [(1, 'black'), (8, 'white')]
        for (row, color) in row_color_zipped:
            for col in self.game_board.cols:
                field = self.game_board.get_field(col, row)
                if field.get_Piece() is not None:
                    piece = field.get_Piece()
                    if piece.get_piece_type() == 'pawn' and piece.player_color == color:
                        piece.upgrade_piece()