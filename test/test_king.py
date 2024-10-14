import unittest
from ajedrez.king import King
from ajedrez.board import Board
from ajedrez.rook import Rook


class TestKing(unittest.TestCase):
    def test_white_king(self):
        white_king = King("WHITE")
        self.assertEqual(str(white_king), "♔")

    def test_black_king(self):
        black_king = King("BLACK")
        self.assertEqual(str(black_king), "♚")

    def setUp(self):
        # Tablero vacío de 8x8 (None representa una casilla vacía)
        self.empty_board = [[None for _ in range(8)] for _ in range(8)]
        self.board = Board()
        self.rook = Rook("BLACK")
    
    def test_king_valid_move(self):
        king = King("WHITE")
        # Movimiento válido de una casilla en cualquier dirección
        self.assertTrue(king.can_move(4, 4, 5, 5, self.empty_board))  # Diagonal
        self.assertTrue(king.can_move(4, 4, 4, 5, self.empty_board))  # Horizontal
        self.assertTrue(king.can_move(4, 4, 5, 4, self.empty_board))  # Vertical

    def test_king_cannot_capture_own_piece(self):
        king = King("WHITE")
        # Colocamos una pieza del mismo color en la casilla de destino
        self.empty_board[5, 5] = King("WHITE")
        # El rey no puede capturar su propia pieza
        self.assertFalse(king.can_move(4, 4, 5, 5, self.empty_board))

    def test_king_cannot_move_out_of_the_board(self):
        king = King("WHITE")
        # El rey no puede moverse fuera del tablero
        self.assertFalse(king.can_move(4, 4, 0, 0, self.empty_board))
        self.assertFalse(king.can_move(4, 4, 9, 9, self.empty_board))

    def test_king_cannot_move_into_check():
        king = King("WHITE")
        enemy_rook = Rook("BLACK")
        board = Board()
        board.place_piece(king, 4, 4)
        board.place_piece(enemy_rook, 4, 6)  # La torre negra amenaza la fila 4

        # El rey no puede moverse hacia la casilla 4,5 ya que está bajo ataque
        assert king.can_move(4, 4, 4, 5, board) == False

        # El rey no puede moverse hacia la casilla 4,6 ya que está bajo ataque
        assert king.can_move(4, 4, 4, 6, board) == False

    def test_king_move_into_check(self):
        king = King("WHITE")
        enemy_rook = Rook("BLACK")
        board = Board()
        board.place_piece(king, 4, 4)
        board.place_piece(enemy_rook, 4, 6)  # La torre negra amenaza la fila 4

        # El rey puede moverse hacia la casilla 4,5 ya que está bajo ataque
        assert king.can_move(4, 4, 4, 5, board) == True

        # El rey puede moverse hacia la casilla 4,6 ya que está bajo ataque
        assert king.can_move(4, 4, 4, 6, board) == True


if __name__ == '__main__':
    unittest.main()






