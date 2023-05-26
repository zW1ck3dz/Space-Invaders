""" Fichier laser """

from turtle import Turtle, register_shape

def affiche_laser(heros):
    """ Fonction qui crée le laser """
    laser = Turtle()
    register_shape("laser.gif")
    laser.shape("laser.gif")
    laser.penup()
    laser.hideturtle()
    laser.speed(0)
    laser.setposition(heros.xcor(), heros.ycor() + 35)
    laser.showturtle()

    return laser


def mouvement_laser(laser, heros, v_laser):
    """ Fonction qui définis le mouvement du laser """
    y_laser = laser.ycor()
    y_laser += v_laser
    laser.sety(y_laser)
    if y_laser > 350:
        laser.hideturtle()
        laser.setposition(heros.xcor(), heros.ycor() + 35)
        laser.showturtle()
