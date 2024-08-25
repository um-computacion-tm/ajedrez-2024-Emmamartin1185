from ajedrez.rook import Rook
from ajedrez.pawn import Pawn
from ajedrez.king import King  
from ajedrez.horse import Horse
from ajedrez.bishop import Bishop
from ajedrez.queen import Queen

class Board:
    def __init__(self):
        self.__positions__ = [[None for _ in range(8)] for _ in range(8)]

        # Coloca las torres
        self.__positions__[0][0] = Rook("BLACK")
        self.__positions__[0][7] = Rook("BLACK")
        self.__positions__[7][0] = Rook("WHITE")
        self.__positions__[7][7] = Rook("WHITE")

        # Coloca los peones
        for col in range(8):
            self.__positions__[1][col] = Pawn("BLACK")
            self.__positions__[6][col] = Pawn("WHITE")

        # Coloca los reyes
        self.__positions__[0][4] = King("BLACK")
        self.__positions__[7][4] = King("WHITE")
        
        # Coloca los caballos 
        self.__positions__[0][1] = Horse("BLACK")
        self.__positions__[0][6] = Horse("BLACK")
        self.__positions__[7][1] = Horse("WHITE")
        self.__positions__[7][6] = Horse("WHITE") 

        #Coloca los alfil
        self.__positions__[0][2] = Bishop("BLACK")
        self.__positions__[0][5] = Bishop("BLACK")
        self.__positions__[7][2] = Bishop("WHITE")
        self.__positions__[7][5] = Bishop("WHITE")

        #Coloca las reinas
        self.__positions__[0][3] = Queen("BLACK")
        self.__positions__[7][3] = Queen("WHITE")

    def get_piece(self, row, col):
        return self.__positions__[row][col]

    def __str__(self): 
        rows = []
        for row in self.__positions__:
            row_str = ""
            for piece in row:
                row_str += str(piece) if piece else " "
            rows.append(row_str)
        return "\n".join(rows)

if __name__ == "__main__":
    board = Board()
    print(board)
