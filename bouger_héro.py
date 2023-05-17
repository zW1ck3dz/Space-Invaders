<<<<<<< HEAD
""" Space Invaders - Bouger le héro

fait par Lucas le 16.05.2023 """


def gauche(hero):
    """ Fonction qui sert à bouger le héros vers la gauche """
    x = hero.xcor()
    x -= 40
    
    if x < -320:
        x = -320
        
    hero.setx(x)
    
    
def droit(hero):
    """ Fonction qui sert à bouger le héros vers la droite """
    x = hero.xcor()
    x += 40
    
    if x > 320:
        x = 320
        
=======
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
        
>>>>>>> b09335e794080ae03948b52a237e116ecbe8ca3f
    hero.setx(x)