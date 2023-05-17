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
        
    hero.setx(x)