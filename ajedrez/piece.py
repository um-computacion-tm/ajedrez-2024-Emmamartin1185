class Piece:
    def __init__(self, color):
        if color not in ["BLACK", "WHITE"]:
            raise ValueError("El color debe ser 'BLACK' o 'WHITE'")
        self.color = color

    def __str__(self):
        """Representación en forma de símbolo según el tipo de pieza."""
        raise NotImplementedError("Este método debe ser implementado por las subclases")

    def get_color(self):
        return self.color

