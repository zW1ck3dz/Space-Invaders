""" Space Invaders - Bouger le héro

fait par Lucas le 16.05.2023 """

from turtle import register_shape, Turtle


def affiche_heros():
    """ Fonction qui crée et affiche le héros """
    heros = Turtle()
    register_shape("hero.gif")
    heros.shape("hero.gif")
    heros.penup()
    heros.speed(0)
    heros.setposition(0, -300)

    return heros


def gauche(heros):
    """ Fonction qui sert à bouger le héros vers la gauche """
    coordonnee_x = heros.xcor()
    coordonnee_x -= 40
    coordonnee_x = max(coordonnee_x, -320)
    heros.setx(coordonnee_x)


def droit(heros):
    """ Fonction qui sert à bouger le héros vers la droite """
    coordonnee_x = heros.xcor()
    coordonnee_x += 40
    coordonnee_x = min(coordonnee_x, 320)
    heros.setx(coordonnee_x)
