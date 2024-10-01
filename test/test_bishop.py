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
    
    def test_bishop_path_blocked(self):
        bishop = Bishop("WHITE")
        # Colocamos una pieza en el camino
        self.empty_board[1][1] = Bishop("BLACK")
        # Movimiento bloqueado en diagonal
        self.assertFalse(bishop.can_move(0, 0, 2, 2, self.empty_board))
 
    def test_bishop_captures_opponent(self):
        bishop = Bishop("WHITE")
        # Colocamos una pieza del oponente en el destino
        self.empty_board[2][2] = Bishop("BLACK")
        # El alfil debe poder capturar la pieza negra
        self.assertTrue(bishop.can_move(0, 0, 2, 2, self.empty_board))
    
    def test_bishop_captures_own_piece(self):
        bishop = Bishop("BLACK")
        # Colocamos una pieza del oponente en el destino
        self.empty_board[2][2] = Bishop("WHITE")
        # El alfil debe poder capturar la pieza blanca
        self.assertTrue(bishop.can_move(0, 0, 2, 2, self.empty_board))

    def test_bishop_long_diagonal_clear(self):
        bishop = Bishop("WHITE")
        # Movimiento válido en una diagonal larga sin obstrucciones
        self.assertTrue(bishop.can_move(0, 0, 7, 7, self.empty_board))

    def test_bishop_long_diagonal_blocked(self):
        bishop = Bishop("WHITE")
        # Colocamos una pieza en el camino en la diagonal
        self.empty_board[3][3] = Bishop("BLACK")
        # El movimiento está bloqueado
        self.assertFalse(bishop.can_move(0, 0, 7, 7, self.empty_board))

    def test_bishop_blocked_by_own_piece(self):
        bishop = Bishop("WHITE")
        # Colocamos una pieza propia en la diagonal
        self.empty_board[1][1] = Bishop("WHITE")
        # El alfil no puede saltar sobre su propia pieza
        self.assertFalse(bishop.can_move(0, 0, 2, 2, self.empty_board))

if __name__ == "__main__":
    unittest.main()