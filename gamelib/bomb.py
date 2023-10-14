import random, pygame
from gamelib.imgloader import *



class Bomb:
    def __init__(self, size:tuple[int, int], counts):
        self.x, self.y = size
        lenght = self.lenght = self.x*self.y
        self.counts = counts
        self.suroundOffsets=[-1, 1, -self.x, self.x, -self.x+1, self.x+1, -self.x-1, self.x-1]
        # self.createGradients()
    
    def __len__(self):
        return self.lenght
    
    def generateBombs(self, index):
        area = [x for x in range(self.lenght) if x not in self.getSuroundIndex(index) and x!=index]
        print(area)
        self.bombs=random.sample(area, self.counts)
        
    def itopos(self, index, torender=False):
        x = index%self.x
        y = index//self.x
        if torender:
            x= x*16+self.boardRCNpos[0]
            y= y*16+self.boardRCNpos[1]
        return x,y
    
    def checkBomb(self, index):
        return index in self.bombs
    
    def getSuroundIndex(self, index):
        raw = [index + i for i in self.suroundOffsets if 0<=index+i<self.lenght]
        raw = [i for i in raw if abs(self.itopos(i)[0]-self.itopos(index)[0])<=1]
        raw = [i for i in raw if abs(self.itopos(i)[1]-self.itopos(index)[1])<=1]
        return raw
    
    def getSuroundBombs(self, index): #Return number of nearby bombs at index
        spos = self.getSuroundIndex(index)
        return len([pos for pos in spos if self.checkBomb(pos)])
    
    def getSurroundGrad(self, index):
        return [(i, self.bombGradients[i]) for i in self.getSuroundIndex(index)]
        
    def createGradients(self):
        bombGradients = []
        for i in range(self.lenght):
            if self.checkBomb(i):
                bombGradients.append(-1)
                continue
            
            bombGradients.append(self.getSuroundBombs(i))
        
        self.bombGradients = bombGradients
    
    