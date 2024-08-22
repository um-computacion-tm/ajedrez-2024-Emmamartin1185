import unittest
from ajedrez.board import Board

class TestBoard(unittest.TestCase):
    def test_initial_board_setup(self):
       
        board = Board()

        
        expected_board = (
            "♜      ♜\n"
            "♟♟♟♟♟♟♟♟\n"
            "        \n"
            "        \n"
            "        \n"
            "        \n"
            "♙♙♙♙♙♙♙♙\n"
            "♖      ♖"
        )

        
        self.assertEqual(str(board), expected_board)

if __name__ == "__main__":
    unittest.main()
