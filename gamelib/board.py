
class Board:
    def __init__(self, size: int) -> None:
        self.size = size
        self.opened = []
        self.flagged = []
        self.boardRCNpos = (5,50) #Right Corner pos of the board area
    
    def checkopened(self, index):
        return index in self.opened
    
    def openOne(self, index):
        self.opened.append(index)

    def open(self, index):
        pass
    
    def flag(self, index):
        self.flagged.append(index)
    
    def checkflagged(self, index):
        return index in self.flagged
    
    def checkmouse(self, pos:tuple[int,int]): #check if mouse's pos is within the board
        x_valid =  self.boardRCNpos[0] <=pos[0]<= self.boardRCNpos[0]+self.x*16
        y_valid =  self.boardRCNpos[1] <=pos[1]<= self.boardRCNpos[1]+self.y*16
        
        return x_valid and y_valid
    