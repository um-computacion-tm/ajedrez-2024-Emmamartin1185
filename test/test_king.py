import unittest
from ajedrez.king import King

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
    
    def test_king_valid_move(self):
        king = King("WHITE")
        # Movimiento válido de una casilla en cualquier dirección
        self.assertTrue(king.can_move(4, 4, 5, 5, self.empty_board))  # Diagonal
        self.assertTrue(king.can_move(4, 4, 4, 5, self.empty_board))  # Horizontal
        self.assertTrue(king.can_move(4, 4, 5, 4, self.empty_board))  # Vertical

if __name__ == '__main__':
    unittest.main()






