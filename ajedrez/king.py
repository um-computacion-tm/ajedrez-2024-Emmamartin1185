class King:
    def __init__(self, color):
        self.color = color

    def __str__(self):
       
        return "♔" if self.color == "WHITE" else "♚"  
    
    def move(self, board, move):
        pass

