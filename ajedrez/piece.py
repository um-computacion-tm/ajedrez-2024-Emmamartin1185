class Piece:
    def __init__(self, color):
        if color not in ["BLACK", "WHITE"]:
            raise ValueError("El color debe ser 'BLACK' o 'WHITE'") #Por si no pone el color bien: crear excepción
        self.color = color

    def __str__(self):
        """Representación en forma de símbolo según el tipo de pieza."""
        raise NotImplementedError("Este método debe ser implementado por las subclases")

    def get_color(self):
        return self.color 
   
    def can_move(self, from_row, from_col, to_row, to_col, board):
        raise NotImplementedError("Este método debe ser implementado por las subclases")


