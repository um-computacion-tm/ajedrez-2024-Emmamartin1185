import unittest
from ajedrez.board import Board

class TestBoard(unittest.TestCase):
    def test_initial_board_setup(self):
        # Crea una instancia del tablero
        board = Board()

        # Representación esperada del tablero con todas las piezas iniciales, incluyendo los Reyes
        expected_board = (
            "♜♞  ♚ ♞♜\n"  # Filas de las piezas negras con Rey incluido
            "♟♟♟♟♟♟♟♟\n"
            "        \n"
            "        \n"
            "        \n"
            "        \n"
            "♙♙♙♙♙♙♙♙\n"
            "♖♘  ♔ ♘♖"   # Filas de las piezas blancas con Rey incluido
        )

        # Compara la salida del tablero actual con la esperada
        self.assertEqual(str(board), expected_board)

if __name__ == "__main__":
    unittest.main()
