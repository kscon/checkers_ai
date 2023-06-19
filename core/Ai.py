from treelib import tree, node
import random
from core.Board import Board


class Ai:
    color = 0  # white=0, black=1
    method = 'random'
    # gd = None
    game_board = None
    depth = None

    def __init__(self, color, game_board: Board, depth: int = 3):
        # self.gd = gamedriver
        self.color = color
        self.game_board = game_board
        self.depth = depth

    def get_move(self, board: Board):
        self.game_board = board
        move = ''
        list_of_moves = self.enumerate_moves()
        move = self.execute_strategy(list_of_moves)
        return move

    def enumerate_moves(self):
        list_of_moves = []  # in the fashion of = ['a3b4', 'c3b5', ...]
        play_direction = 1
        if self.color == 1:
            play_direction = -1

        for col in self.game_board.cols:
            for row in self.game_board.rows:
                field = self.game_board.get_field(col, row)
                if field.get_Piece() is not None:
                    piece = field.get_Piece()
                    if self.color == 0 and piece.player_color == 'white' or \
                            self.color == 1 and piece.player_color == 'black':
                        if piece.get_piece_type() == 'pawn':
                            # enumerate possible moves
                            for col_dif in [-1, 1]:
                                for row_dif in [1, 2]:
                                    target_col = chr(ord(col) - row_dif * col_dif)
                                    target_row = row + row_dif * play_direction
                                    # if 60 <= ord(target_col) <= 68 and 1 <= target_row <= 8:
                                    is_valid = self.game_board.try_move(self.color, col + str(row),
                                                                        target_col + str(target_row))
                                    if is_valid == 1:
                                        list_of_moves.append(col + str(row) + target_col + str(target_row))
                        elif piece.get_piece_type() == 'queen':
                            for col_dir in [-1, 1]:
                                for row_dir in [-1, 1]:
                                    for distance in range(1, 8):
                                        target_col = chr(ord(col) + col_dir * distance)
                                        target_row = row + row_dir * distance
                                        if target_row < 1 or target_row > 8 or ord(target_col) < 97:
                                            continue
                                        is_valid = self.game_board.try_move(self.color, col + str(row),
                                                                            target_col + str(target_row))
                                        if is_valid == 1:
                                            list_of_moves.append(col + str(row) + target_col + str(target_row))

        return list_of_moves

    def execute_strategy(self, list_of_moves):
        if self.method == 'random':
            print(self.minmax_evaluate_board())
            return random.choice(list_of_moves)
        elif self.method == 'minmax':
            pass  # todo

    # minmax algorithm
    def minmax(self):
        own_color = self.color
        move_tree = tree()
        tree.create_node('root', 'root')
        for d in range(self.depth):
            list_of_moves = self.enumerate_moves()
            for m in list_of_moves:
                pass  # todo

    # core method of minmax to find the best move
    def minmax_evaluate_board(self):
        board_evaluation = 0
        for col in self.game_board.cols:
            for row in self.game_board.rows:
                field = self.game_board.get_field(col, row)
                if field.get_Piece() is not None:
                    piece = field.get_Piece()
                    if piece.get_piece_type() == 'pawn':
                        if self.color == 0 and piece.player_color == 'white' or \
                                self.color == 1 and piece.player_color == 'black':
                            board_evaluation += 1
                        else:
                            board_evaluation -= 1
                    elif piece.get_piece_type() == 'queen':
                        if self.color == 0 and piece.player_color == 'white' or \
                                self.color == 1 and piece.player_color == 'black':
                            board_evaluation += 2
                        else:
                            board_evaluation -= 2
        if self.color == 1:
            board_evaluation = -1*board_evaluation
        return board_evaluation
