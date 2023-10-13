from gamelib import Bomb, Board
from gamelib.imgloader import *
import pygame

pygame.display.init()


class gameRenderer(Bomb, Board, pygame.Surface):
    def __init__(self, size: tuple[int, int], counts):
        Bomb.__init__(self, size=size, counts=counts)
        Board.__init__(self, size=size)
        pygame.Surface.__init__(self, (self.x*16+10, self.y*16+55), pygame.SRCALPHA, 32)
        self.failed=False
        
    def background(self):
        self.fill((128, 128, 128))
    
    # i = index, pos = position
    def itopos(self, index, torender=False):
        x = index%self.x
        y = index//self.x
        if torender:
            x= x*16+self.boardRCNpos[0]
            y= y*16+self.boardRCNpos[1]
        return x,y

    def postoi(self, pos, raw=False):
        a, b = pos
        if raw:
            a-=self.boardRCNpos[0]
            b-=self.boardRCNpos[1]
            a%=16
            b%=16
        
        return a + b*16
            
    def drawGround(self):
        
        for i, grad in enumerate(self.bombGradients):
            if grad==-1:
                self.blit(MINE, self.itopos(i, True))
                continue
            if grad==-2:
                self.blit(EXPLODED, self.itopos(i, True))
            if grad==0:
                self.blit(EMPTY, self.itopos(i, True))
                continue
            self.blit(NUMTILES[grad], self.itopos(i, True))
        
        
    
    def drawboard(self):        
        for i in range(self.lenght):
            if not self.checkopened(i):
                self.blit(UNKNOWN, self.itopos(i, True))
                
    def draw(self):
        self.background()
        # self.drawboard()
        self.drawGround()
        
        if self.failed:
            self.blit(self.self, self.boardRCNpos)
        
        self.convert_alpha()