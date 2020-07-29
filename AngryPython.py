# -*- coding: utf-8 -*-
"""
Created on Sat May  9 20:42:18 2020
@author: Matheus Ruggeri
"""

import pygame.gfxdraw
import pygame
import sys
import memorycard
import imgblit
 

sizeX = 1024
sizeY = 800
tileSize = 32

# Initiate the pygame, the font, display and clock
pygame.init()
backgroundLayer = pygame.display.set_mode((sizeX, sizeY))
tileLayer = pygame.display.set_mode((sizeX, sizeY))
charLayer = pygame.display.set_mode((sizeX, sizeY))
snakeLayer = pygame.display.set_mode((sizeX, sizeY))

clock = pygame.time.Clock()
clock.tick(60)
pygame.display.set_caption("Angry Python")


backgroundLayer.fill((255,0,0))
backgroundTiles = {0: imgblit.background("empty")}
backgroundTiles.update({1: imgblit.background("grassCenter")})
backgroundTiles.update({2: imgblit.background("grassCliff_left")})
backgroundTiles.update({3: imgblit.background("grassCliff_right")})
backgroundTiles.update({4: imgblit.background("grassMid")})

generalTiles = {1: imgblit.tiles("slingshotTop")}
generalTiles.update({2: imgblit.tiles("slingshotY")})
generalTiles.update({3: imgblit.tiles("slingshotPipe")})
generalTiles.update({4: imgblit.tiles("brickGrey")})

opponentTiles = {1: imgblit.opponents("snake")}
opponentTiles.update({2: imgblit.opponents("pig")})
opponentTiles.update({3: imgblit.opponents("hippo")})
opponentTiles.update({4: imgblit.opponents("giraffe")})

currentLevel = memorycard.loadLevel(1, 'background')
x = 0; y = 0;
for elementList in currentLevel:
    for element in elementList:
        element = int(element)
        backgroundTiles[element].draw(backgroundLayer, x, y)
        x += tileSize
    y += tileSize
    x = 0
    
currentLevel = memorycard.loadLevel(1, 'elements')
x = 0; y = 0;
for elementList in currentLevel:
    for element in elementList:
        element = int(element)
        if element != 0:
            generalTiles[element].draw(tileLayer, x, y)
        x += tileSize
    y += tileSize
    x = 0
    
currentLevel = memorycard.loadLevel(1, 'opponents')
x = 0; y = 0;
for elementList in currentLevel:
    for element in elementList:
        element = int(element)
        if element != 0:
            opponentTiles[element].draw(charLayer, x, y)
        x += tileSize
    y += tileSize
    x = 0
    
pygame.display.update()
x = 150; y = 350
while (x < 800):
    x += 1
    opponentTiles[1].draw(snakeLayer, x, y)
    pygame.time.wait(3)
    pygame.display.update()
    
print ("finished")

finished = 1
while (not finished):
    pass
        
# Print the thanks, wait 2 seconds and quit
def quit_game():
    pygame.time.wait(1000)
    pygame.quit()
    sys.exit(0)

quit_game()