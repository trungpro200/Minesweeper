import random, pygame
from gamelib.imgloader import *

class Bomb:
    def __init__(self, size:tuple[int, int], counts):
        self.x, self.y = size
        lenght = self.lenght = self.x*self.y
        self.counts = counts
        self.bombs = random.sample(range(lenght), counts)
        self.suroundOffsets=[-1, 1, -self.x, self.x, -self.x+1, self.x+1, -self.x-1, self.x-1]
        self.createGradients()
    
    def __len__(self):
        return self.lenght
    
    def checkBomb(self, index):
        return index in self.bombs
    
    def getSuroundIndex(self, index):
        return [index + i for i in self.suroundOffsets if 0<=index+i<self.lenght]
    
    def getSuroundBombs(self, index): #Return number of nearby bombs at index
        spos = self.getSuroundIndex(index)
        return len([pos for pos in spos if self.checkBomb(pos)])
    
    def createGradients(self):
        bombGradients = []
        for i in range(self.lenght):
            if self.checkBomb(i):
                bombGradients.append(-1)
                continue
            
            bombGradients.append(self.getSuroundBombs(i))
        
        self.bombGradients = bombGradients
    
    