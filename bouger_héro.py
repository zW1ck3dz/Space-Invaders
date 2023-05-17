""" Space Invaders - Bouger le héro

fait par Lucas le 16.05.2023 """

import turtle

def gauche(hero):
    """Décaler le joueur à gauche."""
    x = hero.xcor()
    
    if x < -320:
        x = -320
    else:
        x -= 30
        
    hero.setx(x)
    

def droit(hero):
    """Décaler le joueur à droite."""
    x = hero.xcor()
    x += 30
    
    if x > 320:
        x = 320
    else:
        x += 30
        
    hero.setx(x)