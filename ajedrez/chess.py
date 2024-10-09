from ajedrez.rook import Rook
from ajedrez.horse import Horse
from ajedrez.bishop import Bishop
from ajedrez.queen import Queen
from ajedrez.king import King
from ajedrez.pawn import Pawn

class Chess:   
    def __init__(self):
        # Inicializar el tablero con las piezas en sus posiciones iniciales
        self.board = self.create_initial_board()
        self.turn = "WHITE"  # El turno inicial es de las blancas
    
    def create_initial_board(self):
     
     return [
        [Rook("BLACK"), Horse("BLACK"), Bishop("BLACK"), Queen("BLACK"), King("BLACK"), Bishop("BLACK"), Horse("BLACK"), Rook("BLACK")],
        [Pawn("BLACK"), Pawn("BLACK"), Pawn("BLACK"), Pawn("BLACK"), Pawn("BLACK"), Pawn("BLACK"), Pawn("BLACK"), Pawn("BLACK")],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [Pawn("WHITE"), Pawn("WHITE"), Pawn("WHITE"), Pawn("WHITE"), Pawn("WHITE"), Pawn("WHITE"), Pawn("WHITE"), Pawn("WHITE")],
        [Rook("WHITE"), Horse("WHITE"), Bishop("WHITE"), Queen("WHITE"), King("WHITE"), Bishop("WHITE"), Horse("WHITE"), Rook("WHITE")],
    ]

    
    def show_board(self):
        """
        Muestra el tablero de ajedrez de forma legible en la terminal.
        """
        display = ""
        for row in range(8):
            display += f"{8 - row} "  # Números de fila
            for col in range(8):
                piece = self.board[row][col]
                if piece is None:
                    display += ". "  # Representación de una casilla vacía
                else:
                    display += str(piece) + " "  # Representación de la pieza
            display += "\n"
        display += "  a b c d e f g h"  # Letras de las columnas
        return display

    def move(self, from_row, from_col, to_row, to_col):
        # Aquí va la lógica de mover una pieza (debes implementarla).
        pass

    def is_playing(self):
        return self.turn == "WHITE"
    
    def show_board(self):
        """
        Muestra el tablero de ajedrez de forma legible en la terminal.
        """
        display = ""
        for row in range(8):
            display += f"{8 - row} "  # Números de fila
            for col in range(8):
                piece = self.board[row][col]
                if piece is None:
                    display += ". "  # Representación de una casilla vacía
                else:
                    display += str(piece) + " "  # Representación de la pieza
            display += "\n"
        display += "  a b c d e f g h"  # Letras de las columnas
        return display
        
          
    