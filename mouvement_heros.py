""" Space Invaders - Bouger le héro

fait par Lucas le 16.05.2023 """


def gauche(hero):
    """ Fonction qui sert à bouger le héros vers la gauche """
    coordonnee_x = hero.xcor()
    coordonnee_x -= 40
    coordonnee_x = max(coordonnee_x, -320)
    hero.setx(coordonnee_x)


def droit(hero):
    """ Fonction qui sert à bouger le héros vers la droite """
    coordonnee_x = hero.xcor()
    coordonnee_x += 40
    coordonnee_x = min(coordonnee_x, 320)
    hero.setx(coordonnee_x)
