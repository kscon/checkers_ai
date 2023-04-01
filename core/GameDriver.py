from core.Board import Board
from core.Ai import Ai
import random


class GameDriver:
    game_board = Board()
    current_player = 0  # white=0, black=1
    game_over = 0  # 0 as long as game is going on, 1 if finished
    human_player_color = 0
    ai = Ai()

    def game_loop(self, players=[]):
        self.prepare_game()
        while not self.game_over:
            if self.human_player_color == self.current_player:
                player_move = input('make a move in the form \'a3b4\'...')
                while self.make_move(player_move[:2], player_move[2:]) == -1:
                    player_move = input('try again...')
            else:
                ai_move = self.ai.get_move(self.game_board)
                self.make_move(ai_move[:2], ai_move[2:])
            self.print_board()

    def prepare_game(self):
        print('Play checkers against the AI!')
        if random.random() > 0.5:
            self.human_player_color = 1
            print('you play the black pieces')
        else:
            print('you play the white pieces')

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

        res = self.game_board.is_valid_move(self.current_player, source_col, source_row, target_col, target_row)
        if res[0] == 1:
            self.game_board.move_piece(source_col, source_row, target_col, target_row)
            if res[1] is not None:
                self.game_board.remove_piece(res[1].col, res[1].row)
            self.current_player = (self.current_player + 1) % 2
        else:
            print('Move ' + source_field + '->' + target_field + ' is not legal!')
            return -1

    # expects valid source and target field (i.e., on the board),
    # validation of the move itself is done here
    # returns: (code, field), where field depicts a checked piece or None, and code
    # -1 for an invalid move
    # 1 for a vaild move


gd = GameDriver()
# gd.game_loop()
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
