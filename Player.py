class Player:
    def __init__(self, color, PieceNumber):
        self.color = color
        self.PieceNumber = PieceNumber

    def getColor(self):
        return self.color
      
    def getPieceNumber(self):
        return self.PieceNumber
    
    def updatePieceNum(self):
        self.PieceNumber = self.PieceNumber - 1