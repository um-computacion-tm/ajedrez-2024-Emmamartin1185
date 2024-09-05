from ajedrez.bishop import Bishop
import unittest
class TestBishop(unittest.TestCase):
    def setUp(self):
        # Tablero vacío de 8x8 (None representa una casilla vacía)
        self.empty_board = [[None for _ in range(8)] for _ in range(8)]
 
    def test_bishop_valid_move_diagonal(self):
        bishop = Bishop("WHITE")
        # Movimiento válido en diagonal
        self.assertTrue(bishop.can_move(0, 2, 3, 5, self.empty_board))