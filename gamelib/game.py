from gamelib import Bomb, Board
from gamelib.imgloader import *
import pygame

pygame.display.init()


class gameRenderer(Bomb, Board, pygame.Surface):
    def __init__(self, size: tuple[int, int], counts):
        Bomb.__init__(self, size=size, counts=counts)
        Board.__init__(self, size=size)
        pygame.Surface.__init__(self, (self.x*16+10, self.y*16+55), pygame.SRCALPHA, 32)
        self._resetbutton = self.blit(RESTART, ((self.x-2)*8+5, 10))
        self.failed=False
        self.init_index=None
        
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
            a=a-self.boardRCNpos[0]
            b=b-self.boardRCNpos[1]
            a=a//16
            b=b//16
        
        return a + b*self.x
            
    def drawGround(self):
        if not self.init_index:
            return
        
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
        
    def openOne(self, index):
        if index in self.opened:
            return
        self.opened.append(index)

    def openClear(self, index):
        surGrad = self.getSurroundGrad(index)
        self.openOne(index)
        for i, grad in surGrad:
            if grad!=0:
                self.openOne(i)
                continue
            if grad==0:
                if i in self.opened:
                    continue
                self.openClear(i)
    
    def adjFlag(self, index):
        return len([x for x in self.getSuroundIndex(index) if x in self.flagged])
    
    def adjOpened(self, index):
        return len([x for x in self.getSuroundIndex(index) if x in self.opened])
    
    def openAuto(self, index):
        if self.adjFlag(index)==self.bombGradients[index]:
            [self.open(x, auto=True) for x in self.getSuroundIndex(index) if x not in self.flagged]
    
    def flagAuto(self, index):
        if 8-self.adjOpened(index)==self.bombGradients[index]:
            [self.toggle_flag(x) for x in self.getSuroundIndex(index) if x not in self.flagged and x not in self.opened]
        
    def open(self, index, auto=False):
        if self.checkBomb(index):
            self.failed=True
            return
        
        if self.checkopened(index) and not auto:
            self.openAuto(index)
            self.flagAuto(index)
        
        if self.bombGradients[index]!=0:
            self.openOne(index)
            return
        self.openClear(index)
    
    def toggle_flag(self, index):
        if self.checkflagged(index):
            self.flagged.remove(index)
            return
        self.flagged.append(index)    
    
    def drawboard(self):        
        for i in range(self.lenght):
            
            if self.checkopened(i):
                continue
            
            if self.checkflagged(i):
                self.blit(FLAG, self.itopos(i, True))
                continue
            
            self.blit(UNKNOWN, self.itopos(i, True))
    def drawbutton(self):
        self.blit(RESTART, ((self.x-2)*8+5, 10))
        
    def draw(self):
        self.background()
        self.drawGround()
        if not self.failed:
            self.drawboard()
        self.drawbutton()
        self.convert_alpha()