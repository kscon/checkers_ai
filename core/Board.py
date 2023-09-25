from treelib import Tree, Node
import copy
from core.Field import Field
from core.Piece import Piece
from core.Board_State import BoardState

class Board:
    board = {}
    cols = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    rows = [1, 2, 3, 4, 5, 6, 7, 8]
    current_player = 0  # white=0, black=1
    # log_of_moves = []
    current_node_id = 0  #
    board_history = None


    def __init__(self, scenario=None):
        self.init_board()
        self.init_pieces(scenario)
        self.board_history = Tree()
        self.board_history.create_node(0, 0, data=BoardState(copy.deepcopy(self.board), [], 0, {}, 0))

    def init_board(self):
        for col in self.cols:
            for row in self.rows:
                self.board[(col, row)] = Field(col, row)

    def init_pieces(self, scenario):
        if scenario is None:
            # white pieces
            for row in [1, 3]:
                for col in ['a', 'c', 'e', 'g']:
                    self.get_field(col, row).set_Piece(Piece('white', 'pawn'))
            for col in ['b', 'd', 'f', 'h']:
                self.get_field(col, 2).set_Piece(Piece('white', 'pawn'))

            # black pieces
            for row in [6, 8]:
                for col in ['b', 'd', 'f', 'h']:
                    self.get_field(col, row).set_Piece(Piece('black', 'pawn'))
            for col in ['a', 'c', 'e', 'g']:
                self.get_field(col, 7).set_Piece(Piece('black', 'pawn'))
        else:
            for (col, row, piece_color, piece_type) in scenario:
                field = self.get_field(col, row)
                assert field is not None
                assert field.get_Piece() is None
                field.set_Piece(Piece(piece_color,piece_type))


    def get_field(self, col, row):
        return self.board[(col, row)]

    def get_field_by_index(self, col_index, row_index):
        return self.board[(self.cols[col_index], self.rows[row_index])]

    def board_to_string(self):
        s = ""
        for row in reversed(self.rows):
            for col in self.cols:
                piece = self.get_field(col, row).get_Piece()
                if piece is not None:
                    s += '|' + piece.to_string()
                else:
                    s += '| '
            s += '|\n'

        return s

    # set board to a state from board_history
    # this method does not change the board_history
    def reset_board_to_board_history_node(self, board_history_node_id):
        node = self.board_history.get_node(board_history_node_id)
        self.board = copy.deepcopy(node.data.board)
        self.current_node_id = board_history_node_id
        self.current_player = node.data.current_player

    # interface for trying moves on the board
    def try_move(self, player_color, source_field, target_field):
        source_col, source_row = source_field
        target_col, target_row = target_field
        return self.is_valid_move(player_color, source_col, source_row, target_col, target_row)[0]
        # if res[0] == 1:
        #     self.move_piece(source_col, source_row, target_col, target_row)
        #     if res[1] is not None:
        #         self.remove_piece(res[1].col, res[1].row)
        #     self.current_player = (self.current_player + 1) % 2
        # else:
        #     print('Move ' + source_field + '->' + target_field + ' is not legal!')
        #     return -1

    # interface for making moves on the board
    def make_move(self, player_color, source_field, target_field):
        if player_color != self.current_player:
            print('Player color of move and current player data are not the same!')
            return -1
        source_col, source_row = source_field
        target_col, target_row = target_field
        res = self.is_valid_move(self.current_player, source_col, source_row, target_col, target_row)
        if res[0] == 1:
            self.move_piece(source_col, int(source_row), target_col, int(target_row))

            # data for new BoardState node in board history tree
            checked_piece = ()

            if res[1] is not None:
                checked_piece = (
                self.get_field(res[1].col, res[1].row).get_Piece().to_string(), res[1].col + str(res[1].row))
                self.remove_piece(res[1].col, res[1].row)
            self.current_player = (self.current_player + 1) % 2

            # data for new BoardState node in board history tree
            current_node = self.board_history.get_node(self.current_node_id)
            turn = current_node.data.turn + 1
            board = copy.deepcopy(self.board)
            move = source_field + target_field
            move_log = current_node.data.move_log.copy()
            move_log.append(move)
            checked_pieces_dict = current_node.data.checked_pieces.copy()
            checked_pieces_dict[turn] = checked_piece

            # add new board history node
            self.current_node_id += 1
            while self.board_history.get_node(self.current_node_id) is not None:
                self.current_node_id += 1
            self.board_history.create_node(self.current_node_id, self.current_node_id,
                                           parent = current_node.identifier,
                                           data=BoardState(board, move_log, self.current_player, checked_pieces_dict,
                                                           turn))

        else:
            print('Move ' + source_field + '->' + target_field + ' is not legal!')
            return -1

    # does NOT check for validity
    # expects sanitized input
    def move_piece(self, source_col, source_row, target_col, target_row):
        source_field = self.get_field(source_col, source_row)
        target_field = self.get_field(target_col, target_row)
        piece = source_field.get_Piece()
        target_field.set_Piece(piece)
        source_field.reset_Field()

    # does NOT check for validity
    # expects sanitized input
    def remove_piece(self, target_col, target_row):
        target_field = self.get_field(target_col, target_row)
        target_field.reset_Field()

    # expects valid source and target field (i.e., on the board),
    # validation of the move itself is done here
    # returns: (code, field), where field depicts a checked piece or None, and code
    # -1 for an invalid move
    # 1 for a valid move
    def is_valid_move(self, current_player, source_col, source_row, target_col, target_row):
        try:
            source_row = int(source_row)
            target_row = int(target_row)
            assert isinstance(source_col, str) and source_col in self.cols
            assert isinstance(source_row, int) and source_row in self.rows
            assert isinstance(target_col, str) and target_col in self.cols
            assert isinstance(target_row, int) and target_row in self.rows
        except AssertionError:
            # print('Not a valid field/notation!')
            return -1, None
        piece = self.get_field(source_col, source_row).get_Piece()
        if piece is None:
            return -1, None
        if not ((piece.player_color == 'white' and current_player == 0)
                or (piece.player_color == 'black' and current_player == 1)):
            return -1, None
        col_index_source = self.cols.index(source_col)
        row_index_source = self.rows.index(source_row)
        col_index_target = self.cols.index(target_col)
        row_index_target = self.rows.index(target_row)
        checked_field = ' '

        play_direction = 1  # 1 for white, -1 for black
        if current_player == 1:
            play_direction = -1

        # pawn moves
        if piece.get_piece_type() == 'pawn':
            # normal moves
            if abs(col_index_source - col_index_target) == 1:
                target_field = self.get_field(target_col, target_row)
                if target_row - source_row == play_direction and target_field.get_Piece() is None:
                    return 1, None

            # checking moves
            elif abs(col_index_source - col_index_target) == 2:
                # checking move left forward
                target_field = self.get_field(target_col, target_row)
                if target_row - source_row == 2 * play_direction and \
                        target_field.get_Piece() is None:
                    checked_field = self.get_field_by_index(
                        col_index_source + (col_index_target - col_index_source) // 2,
                        row_index_source + play_direction)
                    if checked_field.get_Piece() is None:
                        return -1, None
                    if checked_field.get_Piece().player_color == 'white' and current_player == 1:
                        return 1, checked_field
                    elif checked_field.get_Piece().player_color == 'black' and current_player == 0:
                        return 1, checked_field
        elif piece.get_piece_type() == 'queen':
            if self.get_field(target_col, target_row).get_Piece() is not None:
                return -1, None
            # normal moves (can be as much free fields as possible)
            col_jumped = [i for i in range(min(col_index_source + 1, col_index_target + 1),
                                           max(col_index_source, col_index_target))]
            row_jumped = [i for i in range(min(row_index_source + 1, row_index_target + 1),
                                           max(row_index_source, row_index_target))]

            checked_field = None
            for (c, r) in zip(col_jumped, row_jumped):
                if abs(c - col_index_target) == 1 and self.get_field_by_index(c, r).get_Piece() is not None:
                    checked_field = self.get_field_by_index(c, r)
                    if  (checked_field.get_Piece().get_player_color() == 'white' and current_player == 0) or \
                            (checked_field.get_Piece().get_player_color() == 'black' and current_player == 1):
                        return -1, None
                elif self.get_field_by_index(c, r).get_Piece() is not None:
                    return -1, None
            return 1, checked_field

        # move not valid
        return -1, None

    # upgrade piece
    def check_upgrade_piece(self, target_col, target_row, color):
        target_field = self.get_field(target_col, target_row)
        piece = target_field.get_Piece()
        if piece is not None:
            if piece.get_piece_type() == 'pawn' and piece.player_color == color:
                piece.upgrade_piece()


"""b = Board()
b.init_board()
b.init_pieces()
print(b.board_to_string())
b.move_piece('a', 3, 'b', 4)
print(b.board_to_string())"""
# print(b.board_to_string())
# b.move_piece('A3','B4')
# print(b.board_to_string())