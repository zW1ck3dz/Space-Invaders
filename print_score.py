""" Fichier score """

from turtle import Turtle


def affiche_score():
    """ Fonction qui crée le stylo qui dessinera le score """
    stylo_score = Turtle()
    stylo_score.speed(0)
    stylo_score.color("Lime")
    stylo_score.penup()
    stylo_score.hideturtle()
    stylo_score.goto(0, 400)

    return stylo_score


def point(stylo_score, affiche, score):
    """ Fonction qui augmente le score """
    stylo_score.clear()
    nouveau_score = affiche.format(score)
    stylo_score.write(nouveau_score, move = False, align = "center",
        font = ("Courier" , 30, "bold"))
