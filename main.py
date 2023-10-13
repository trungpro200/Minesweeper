import gamelib
from const import *
import pygame

game = gamelib.gameRenderer((SIZE_X, SIZE_Y), BOMB_COUNT)
win = pygame.display.set_mode((SIZE_X*16+10, SIZE_Y*16+60))

running = True



while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            break
        
        if event.type== pygame.MOUSEBUTTONDOWN:
            
            x, y = pygame.mouse.get_pos()
            
            index = game.postoi((x,y), raw=True)
            
            if event.type == pygame.BUTTON_LEFT:
                game.open(index)
            
            if event.type == pygame.BUTTON_RIGHT:
                pass
    
    game.draw()
    win.blit(game, (0,0))
    
    pygame.display.update()
    
    
    