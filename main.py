import gamelib
from const import *
import pygame


def start():
    global game, win
    game = gamelib.gameRenderer((SIZE_X, SIZE_Y), BOMB_COUNT)
    win = pygame.display.set_mode((SIZE_X*16+10, SIZE_Y*16+60))

game = gamelib.gameRenderer((SIZE_X, SIZE_Y), BOMB_COUNT)
win = pygame.display.set_mode((SIZE_X*16+10, SIZE_Y*16+60))
running = True

while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
        
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if game._resetbutton.collidepoint(x,y):
                    start()
            
            if game.failed: 
                break
            if not game.checkmouse(event.pos):
                break
            
            index = game.postoi((x,y), raw=True)
            
            if event.button == pygame.BUTTON_LEFT:
                if not game.init_index:
                    game.init_index=index
                    game.generateBombs(index)
                    game.createGradients()
                if game.checkflagged(index):
                    break
                game.open(index)
                
            if event.button == pygame.BUTTON_RIGHT:
                game.toggle_flag(index)
        
            
    game.draw()
    win.blit(game, (0,0))
    
    pygame.display.update()
    
    
    