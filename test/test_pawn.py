import unittest
from ajedrez.pawn import Pawn

class TestPawn(unittest.TestCase):
    def test_pawn_representation(self):
        white_pawn = Pawn("WHITE")
        black_pawn = Pawn("BLACK")

        
        self.assertEqual(str(white_pawn), "♙")
        self.assertEqual(str(black_pawn), "♟")
    
    def setUp(self):
        # Tablero vacío de 8x8 (None representa una casilla vacía)
        self.empty_board = [[None for _ in range(8)] for _ in range(8)]

    def test_pawn_initial_double_move_white(self):
        pawn = Pawn("WHITE")
        # Movimiento inicial válido de dos casillas para peón blanco
        self.assertTrue(pawn.can_move(6, 0, 4, 0, self.empty_board))

    def test_pawn_invalid_capture_forward(self):
        pawn = Pawn( "WHITE")
        # Colocamos una pieza del oponente en frente del peón
        self.empty_board[0][5] = Pawn("BLACK")
        # Movimiento inválido porque no puede capturar hacia adelante
        self.assertFalse(pawn.can_move(0, 0, 0, 5, self.empty_board))

    def test_pawn_move_blocked(self):
        pawn = Pawn("WHITE")
        # Colocamos una pieza en frente del peón
        self.empty_board[5][0] = Pawn("BLACK")
        # Movimiento bloqueado (no puede moverse hacia adelante)
        self.assertFalse(pawn.can_move(6, 0, 5, 0, self.empty_board))

    def test_pawn_invalid_double_move_after_first(self):
        pawn = Pawn("WHITE")
        # Movimiento inicial válido
        self.assertTrue(pawn.can_move(6, 0, 4, 0, self.empty_board))
        # Movimiento inválido de dos casillas después del inicial
        self.assertFalse(pawn.can_move(4, 0, 2, 0, self.empty_board))

    def test_pawn_cannot_capture_own_piece(self):
        pawn = Pawn("WHITE")
        # Colocamos una pieza propia en la casilla diagonal
        self.empty_board[5][1] = Pawn("WHITE")
        # Movimiento inválido porque no puede capturar su propia pieza
        self.assertFalse(pawn.can_move(6, 0, 5, 1, self.empty_board))

if __name__ == "__main__":
    unittest.main()    