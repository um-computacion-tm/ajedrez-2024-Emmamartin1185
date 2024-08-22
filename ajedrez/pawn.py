"""
class Pawn:
    def __init__(self, color):
        self.__color__ = color
        self.__symbol__ = "♙" if color == "WHITE" else "♟"
        self.__moved__ = False

    def __str__(self):
        return self.__symbol__

    def valid_moves(self, position, board):
        
        #Retorna una lista de posiciones válidas para mover el peón.
        El movimiento depende del color y si el peón ya se ha movido.
        
        moves = []
        row, col = position

        # Movimiento para peones blancos (hacia arriba)
        if self.__color__ == "WHITE":
            if board.get_piece(row - 1, col) is None:  # Movimiento simple hacia adelante
                moves.append((row - 1, col))
                if not self.__moved__ and board.get_piece(row - 2, col) is None:  # Movimiento doble inicial
                    moves.append((row - 2, col))

        # Movimiento para peones negros (hacia abajo)
        elif self.__color__ == "BLACK":
            if board.get_piece(row + 1, col) is None:  # Movimiento simple hacia adelante
                moves.append((row + 1, col))
                if not self.__moved__ and board.get_piece(row + 2, col) is None:  # Movimiento doble inicial
                    moves.append((row + 2, col))

        return moves

    def move(self):
        self.__moved__ = True
"""      
class Pawn:
    def __init__(self, color):
        self.color = color  # Cambié __color__ a color

    def __str__(self):
        return "♙" if self.color == "WHITE" else "♟"

 