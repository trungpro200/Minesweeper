import pygame
tile = lambda x: pygame.image.load(f'./gamelib/assets/Tile{x}.png')

UNKNOWN = tile('Unknown')
EMPTY = tile('Empty')
MINE = tile('Mine')
EXPLODED = tile('Exploded')
FLAG = tile('Flag')
NUMTILES = {}

for i in range(1,9): 
    NUMTILES[i]=tile(i)