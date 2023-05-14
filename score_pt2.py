"""Projet - Création et affichage du score partie 2

fait le 10/05/2023 par Jason"""
"""Modifié le 14/05/2023"""

import turtle

#Template de ce qui sera affiché
AFFICHE = "Score : {}"

#Mise en place du score initial
score = 0

def score():
    """Création et affichage du score"""
    stylo = turtle.Turtle()
    stylo.speed(0)
    stylo.color("Lime")
    stylo.penup()
    stylo.setposition(0, 400)
    SCORE = AFFICHE.format(score)
    stylo.write(SCORE, move = False, align = "center",
            font = ("Courier" , 30, "bold"))
    stylo.hideturtle()


def point():
    """Mise à jour du score quand une cible est touchée"""
    score += 1
    SCORE = AFFICHE.format(score)
    stylo.clear()
    stylo.write(SCORE, move = False, align = "center",
            font = ("Courier" , 30, "bold"))