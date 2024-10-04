class King:
    def __init__(self, color):
        self.color = color

    def __str__(self):
       
        return "♔" if self.color == "WHITE" else "♚"  
    
    def can_move(self, from_row, from_col, to_row, to_col, board):
        """
        Verifica si el movimiento es válido para el rey.
        El rey puede moverse una casilla en cualquier dirección (horizontal, vertical o diagonal).
        También contempla la posibilidad de enroque.
        """
        row_diff = abs(to_row - from_row)
        col_diff = abs(to_col - from_col)

        # Movimiento normal del rey: una casilla en cualquier dirección
        if row_diff <= 1 and col_diff <= 1:
            return self._is_valid_destination(to_row, to_col, board)

        # Verificar si el movimiento es enroque (castling)
        if not self.has_moved and row_diff == 0 and col_diff == 2:
            return self._is_castling_valid(from_row, from_col, to_row, to_col, board)

        return False

    def _is_valid_destination(self, to_row, to_col, board):
        """
        Verifica si la casilla de destino es válida (vacía o contiene una pieza del oponente).
        """
        destination_piece = board[to_row][to_col]
        if destination_piece is None:
            return True
        elif destination_piece.color != self.color:
            return True  # Captura válida
        return False  # No puede capturar una pieza del mismo color

    def _is_castling_valid(self, from_row, from_col, to_row, to_col, board):
        """
        Verifica si el enroque es válido.
        El enroque solo es válido si:
        - El rey y la torre no se han movido.
        - No hay piezas entre el rey y la torre.
        - El rey no está en jaque, no pasa por una casilla atacada y no termina en jaque.
        """
        # Movimiento enroque corto o largo
        if to_col == from_col + 2:  # Enroque corto (con la torre del lado del rey)
            rook_col = 7
        elif to_col == from_col - 2:  # Enroque largo (con la torre del lado de la reina)
            rook_col = 0
        else:
            return False  # No es un movimiento de enroque

        # Verificar que la torre no se ha movido y que las casillas entre el rey y la torre están vacías
        rook = board[from_row][rook_col]
        if rook is None or rook.__class__.__name__ != "Rook" or rook.has_moved:
            return False

        # Verificar que las casillas entre el rey y la torre están vacías
        step = 1 if to_col > from_col else -1
        for col in range(from_col + step, to_col, step):
            if board[from_row][col] is not None:
                return False

        # Asegurar que el rey no esté en jaque ni pase por una casilla en jaque
        if self._is_in_check(board, from_row, from_col):
            return False
        for col in range(from_col, to_col + step, step):
            if self._is_in_check(board, from_row, col):
                return False

        return True

    
   

