""" Space Invaders - Bouger le héro

fait par Lucas le 16.05.2023 """

import turtle

def gauche(hero):
    x = hero.xcor()
    x -= 30
    
    if x < -320:
        x = -320
        
    hero.setx(x)
    
def droit(hero):
    x = hero.xcor()
    x += 30
    
    if x > 320:
        x = 320
        
    hero.setx(x)