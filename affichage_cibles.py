""" Fichier cibles """

from turtle import Turtle, register_shape
import random


def affiche_cibles(nb_cibles, cibles):
    """ Fonction qui crée et affiche les cibles """
    register_shape("cible.gif")

    for cible in range(nb_cibles):
        cibles.append(Turtle())

    for cible in cibles:
        cible.shape("cible.gif")
        cible.speed(0)
        cible.penup()
        coordonnee_x = random.randint(-300, 300)
        coordonnee_y = random.randint(200, 300)
        cible.setposition(coordonnee_x, coordonnee_y)

    return cible
