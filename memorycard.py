# -*- coding: utf-8 -*-
"""
Created on Sat May  9 20:42:18 2020
@author: Matheus Ruggeri
"""

import csv


# Import the CSV file with all the translations
def loadUserData():
    with open('data/save.csv', mode='r') as infile:
        reader = csv.reader(infile)
        words = {rows[0]: rows[1] for rows in reader}
        return words

def saveUserData():
    pass

def loadLevel(levelNumber, layer):
    if layer == 'background':
        with open('data/level/' + str(levelNumber) + 'b.csv', mode='r') as csvfile:
            data = list(csv.reader(csvfile))

    elif layer == 'elements':
        with open('data/level/' + str(levelNumber) + 'e.csv', mode='r') as csvfile:
            data = list(csv.reader(csvfile))
            
    elif layer == 'opponents':
        with open('data/level/' + str(levelNumber) + 'o.csv', mode='r') as csvfile:
            data = list(csv.reader(csvfile))

    return data