# -*- coding: utf-8 -*-
"""
Created on Sat May  9 20:42:18 2020
@author: Matheus Ruggeri
"""

import pygame

WHITE = (255, 255, 255)

class background(object):
    def __init__(self, name):
        img = pygame.image.load("img/ground/" + name + ".png")
        self.img = pygame.transform.scale(img, (32,32)).convert_alpha()
        
    def draw(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        screen.blit(self.img, pygame.rect.Rect(self.x, self.y, 32, 32)) 
        
class tiles(object):
    def __init__(self, name):
        img = pygame.image.load("img/elements/" + name + ".png").convert_alpha()
        self.img = pygame.transform.scale(img, (32,32)).convert_alpha()
        
    def draw(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        screen.blit(self.img, pygame.rect.Rect(self.x, self.y, 32, 32)) 

class opponents(object):
    def __init__(self, name):
        img = pygame.image.load("img/char/" + name + ".png").convert_alpha()
        self.img = pygame.transform.scale(img, (32,32)).convert_alpha()
        
    def draw(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        screen.blit(self.img, pygame.rect.Rect(self.x, self.y, 32, 32)) 

# Import the CSV file with all the translations
def printLevel():
    pass

def printCharacters():
    pass

def printMovingThings():
    pass
