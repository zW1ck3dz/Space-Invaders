"""Projet - Vérification des collisions

fait le 16/05/2023 par Jason"""

import random


def tuer(cible):
    """ Fonction qui replace la cible lors d'un contacte laser-cible """      
    coordonnee_x = random.randint(-330, 330)
    coordonnee_y = random.randint(200, 300)
    cible.setposition(coordonnee_x, coordonnee_y)
