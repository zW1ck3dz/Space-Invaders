"""Projet - Vérification des collisions

fait le 14/05/2023 par Jason"""

import turtle
import random

def tuer(cible):
    """Replacer la cible au début au contacte avec le laser."""      
    x = random.randint(-330, 330)
    y = random.randint(200, 300)
    cible.setposition(x, y)
    

     