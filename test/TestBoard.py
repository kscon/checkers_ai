import pytest

from core.Board import *
from core.Field import *
from core.Piece import *



class TestBoard:
    board = Board()
    fields_with_pieces = [('a',1),('c',1),('e',1),('g',1),
                              ('b',2),('d',2),('f',2),('h',2),
                              ('a',3),('c',3),('e',3),('g',3),
                              ('b', 6), ('d', 6), ('f', 6), ('h', 6),
                              ('a', 7), ('c', 7), ('e', 7), ('g', 7),
                              ('b', 8), ('d', 8), ('f', 8), ('h', 8),
                              ]

    @pytest.mark.parametrize("col, row",
                             [('a',1),('c',1),('e',1),('g',1),
                              ('b',2),('d',2),('f',2),('h',2),
                              ('a',3),('c',3),('e',3),('g',3),
                              ('b', 6), ('d', 6), ('f', 6), ('h', 6),
                              ('a', 7), ('c', 7), ('e', 7), ('g', 7),
                              ('b', 8), ('d', 8), ('f', 8), ('h', 8),
                              ])
    def test_init_board(self, col, row):
        field = self.board.get_field(col,row)
        assert field.get_col() == col
        assert field.get_row() == row

    @pytest.mark.parametrize("col, row, expected_color, expected_type",
                             [('a', 1, 'white', 'pawn'), ('c', 1, 'white', 'pawn'), ('e', 1, 'white', 'pawn'), ('g', 1, 'white', 'pawn'),
                              ('b', 2, 'white', 'pawn'), ('d', 2, 'white', 'pawn'), ('f', 2, 'white', 'pawn'), ('h', 2, 'white', 'pawn'),
                              ('a', 3, 'white', 'pawn'), ('c', 3, 'white', 'pawn'), ('e', 3, 'white', 'pawn'), ('g', 3, 'white', 'pawn'),
                              ('b', 6,'black', 'pawn'), ('d', 6,'black', 'pawn'), ('f', 6,'black', 'pawn'), ('h', 6,'black', 'pawn'),
                              ('a', 7,'black', 'pawn'), ('c', 7,'black', 'pawn'), ('e', 7,'black', 'pawn'), ('g', 7,'black', 'pawn'),
                              ('b', 8,'black', 'pawn'), ('d', 8,'black', 'pawn'), ('f', 8,'black', 'pawn'), ('h', 8,'black', 'pawn'),
                              ])
    def test_init_pieces(self,col, row, expected_color, expected_type):
        field = self.board.get_field(col, row)
        piece = field.get_Piece()
        assert piece.get_piece_type() == expected_type
        assert piece.get_player_color() == expected_color

    @pytest.mark.parametrize("col", ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
    @pytest.mark.parametrize("row", [1, 2, 3, 4, 5, 6, 7, 8])
    def test_init_pieces_empty_fields(self, col, row):
        if (col, row) not in self.fields_with_pieces:
            field = self.board.get_field(col, row)
            assert field.get_Piece() is None

    @pytest.mark.parametrize("scenario", [[('a',1,'white', 'pawn'),
                                           ('c',3,'white', 'queen'),
                                           ('e',5,'black', 'pawn'),
                                           ('f',6,'black', 'queen')],
                                          [('a', 1, 'white', 'pawn'), ('c', 1, 'white', 'pawn'),
                                           ('e', 1, 'white', 'pawn'), ('g', 1, 'white', 'pawn'),
                                           ('b', 2, 'white', 'pawn'), ('d', 2, 'white', 'pawn'),
                                           ('f', 2, 'white', 'pawn'), ('h', 2, 'white', 'pawn'),
                                           ('a', 3, 'white', 'pawn'), ('c', 3, 'white', 'pawn'),
                                           ('e', 3, 'white', 'pawn'), ('g', 3, 'white', 'pawn'),
                                           ('b', 6, 'black', 'pawn'), ('d', 6, 'black', 'pawn'),
                                           ('f', 6, 'black', 'pawn'), ('h', 6, 'black', 'pawn'),
                                           ('a', 7, 'black', 'pawn'), ('c', 7, 'black', 'pawn'),
                                           ('e', 7, 'black', 'pawn'), ('g', 7, 'black', 'pawn'),
                                           ('b', 8, 'black', 'pawn'), ('d', 8, 'black', 'pawn'),
                                           ('f', 8, 'black', 'pawn'), ('h', 8, 'black', 'pawn'),
                                           ]
                                          ])
    def test_init_pieces_scenario(self, scenario):
        board2 = Board(scenario)
        for (col,row,piece_color, piece_type) in scenario:
            field = board2.get_field(col,row)
            piece = field.get_Piece()
            assert piece.get_piece_type() == piece_type
            assert piece.get_player_color() == piece_color
        fields = [(c, r) for (c,r,a,b) in scenario]
        for col in board2.cols:
            for row in board2.rows:
                if (col, row) not in fields:
                    assert board2.get_field(col, row).get_Piece() is None


    @pytest.mark.parametrize("col, row, ind_col, ind_row",
                             [('a', 1, 0, 0), ('c', 1, 2, 0), ('e', 1, 4, 0),('g', 1, 6, 0),
                              ('b', 2, 1, 1), ('c', 3, 2, 2), ('d', 4, 3, 3), ('e', 5, 4, 4),
                              ('f', 6, 5, 5), ('g', 7, 6, 6), ('h', 8, 7, 7), ('a', 7, 0, 6),
                              ('b', 8, 1, 7), ('g', 1, 6, 0), ('h', 2, 7, 1)
                              ])
    def test_get_field_by_index(self,col,row,ind_col,ind_row):
        assert self.board.get_field(col,row) is self.board.get_field_by_index(ind_col,ind_row)

    @pytest.mark.parametrize("scenario", [[('a', 1, 'white', 'pawn'),
                                           ('c', 3, 'white', 'queen'),
                                           ('e', 5, 'black', 'pawn'),
                                           ('f', 6, 'black', 'queen')]
                                          ])
    def test_board_to_string(self, scenario):
        assert self.board.board_to_string() == "| |b| |b| |b| |b|\n|b| |b| |b| |b| |\n| |b| |b| |b| |b|\n| | | | | | | | |\n| | | | | | | | |\n|w| |w| |w| |w| |\n| |w| |w| |w| |w|\n|w| |w| |w| |w| |\n"
        board2 = Board()
        board2.move_piece('c',3,'d',4)
        board2.move_piece('d',6,'e',5)
        assert board2.board_to_string() == "| |b| |b| |b| |b|\n|b| |b| |b| |b| |\n| |b| | | |b| |b|\n| | | | |b| | | |\n| | | |w| | | | |\n|w| | | |w| |w| |\n| |w| |w| |w| |w|\n|w| |w| |w| |w| |\n"
        board3 = Board(scenario)
        assert board3.board_to_string() == "| | | | | | | | |\n| | | | | | | | |\n| | | | | |B| | |\n| | | | |b| | | |\n| | | | | | | | |\n| | |W| | | | | |\n| | | | | | | | |\n|w| | | | | | | |\n"

    @pytest.mark.parametrize("scenario", [[('a', 1, 'white', 'pawn'),
                                           ('b', 2, 'white', 'pawn'),
                                           ('c', 3, 'white', 'queen'),
                                           ('e', 5, 'black', 'Queen'),
                                           ('f', 6, 'black', 'pawn'),
                                           ('g', 2, 'black', 'pawn')]
                                          ])
    def test_move_piece(self,scenario):
        board2 = Board(scenario)
        board2.move_piece('a', 1, 'b', 2)
        piece = board2.get_field('b',2).get_Piece()
        assert piece.get_piece_type() == 'pawn'
        assert piece.get_player_color() == 'white'
        assert board2.get_field('a',1).get_Piece() is None

        with pytest.raises(KeyError):
            board2.move_piece('g',7, 'i', 9)

    @pytest.mark.parametrize("scenario", [[('a', 1, 'white', 'pawn'),
                                           ('b', 2, 'white', 'pawn'),
                                           ('c', 3, 'white', 'queen'),
                                           ('e', 5, 'black', 'Queen'),
                                           ('f', 6, 'black', 'pawn'),
                                           ('g', 2, 'black', 'pawn')]
                                          ])
    def test_remove_piece(self, scenario):
        board2 = Board(scenario)
        board2.remove_piece('a', 1)
        assert board2.get_field('a', 1).get_Piece() is None

        board2.remove_piece('a', 8)
        assert board2.get_field('a', 8).get_Piece() is None

        with pytest.raises(KeyError):
            board2.remove_piece('i', 9)

    @pytest.mark.parametrize("scenario", [[('a', 1, 'white', 'pawn'),
                                           ('b', 7, 'white', 'pawn'),
                                           ('c', 3, 'white', 'queen'),
                                           ('e', 5, 'black', 'queen'),
                                           ('f', 1, 'white', 'pawn'),
                                           ('f', 6, 'black', 'pawn'),
                                           ('g', 2, 'black', 'pawn')]])
    @ pytest.mark.parametrize("current_player, source_col, source_row, target_col, target_row, expected_output",
                            [(0, 'a', 1, 'b', 2, (1, None)), (0, 'a', 1, 'd', 4, (-1, None)), # pawn
                             (0, 'c', 3, 'b', 2, (1, None)), (0, 'c', 3, 'a', 5, (1, None)), (0, 'c', 3, 'e', 1, (1, None)), # queen
                             (0, 'c', 3, 'e', 5, (-1, None)), (0, 'c', 3, 'f', 6, (-1, None)), (0, 'c', 3, 'g', 7, (-1, None)),
                             (0, 'b', 7, 'a', 8, (1, None))
                             ])
    def test_is_valid_move(self, scenario,current_player, source_col, source_row, target_col, target_row, expected_output):
        board = Board(scenario)
        output = board.is_valid_move(current_player, source_col, source_row, target_col, target_row)
        assert output == expected_output

