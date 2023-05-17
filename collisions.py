<<<<<<< HEAD
"""Projet - Vérification des collisions

fait le 14/05/2023 par Jason"""

import random


def tuer(cible):
    """ Fonction qui replace la cible lors d'un contacte laser-cible """      
    x = random.randint(-330, 330)
    y = random.randint(200, 300)
    cible.setposition(x, y)
   
    





=======
"""Projet - Vérification des collisions

fait le 14/05/2023 par Jason"""

import turtle
import random

def tuer(cible):
    """Replacer la cible au début au contacte avec le laser."""      
    x = random.randint(-330, 330)
    y = random.randint(200, 300)
    cible.setposition(x, y)
    

>>>>>>> b09335e794080ae03948b52a237e116ecbe8ca3f
     