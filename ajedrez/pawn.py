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
        self.color = color  

    def __str__(self):
        return "♙" if self.color == "WHITE" else "♟"

    def valid_moves(self, position, board):
        
        #Retorna una lista de posiciones válidas para mover el peón.El movimiento depende del color y si el peón ya se ha movido.
        
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

    def __is_path_clear__(self, from_row, from_col, to_row, to_col, board):  
     if from_col == to_col:  # Movimiento vertical
            step = 1 if to_row > from_row else -1
            for row in range(from_row + step, to_row, step):
                if board[row][from_col] is not None:
                    return False
                return True
    
     def __can_capture__(self, to_row, to_col, board):
        """
        Verifica si el peón puede capturar una pieza en la casilla destino.
        """
        destination_piece = board[to_row][to_col]
        # Hay una pieza enemiga en la casilla de destino
        if destination_piece is not None and destination_piece.color != self.color:
            return True
        return False