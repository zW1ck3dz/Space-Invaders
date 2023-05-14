"""Projet - Création et affichage du score

fait le 3/05/2023 par Jason"""

import turtle

#Template de ce qui sera affiché
AFFICHE = "Score : {}"

#Mise en place du score initial
score = 0

#Affichage du score
stylo = turtle.Turtle()
stylo.speed(0)
stylo.color("Lime")
stylo.penup()
stylo.setposition(0, 400)
SCORE = AFFICHE.format(score)
stylo.write(SCORE, move = False, align = "center",
            font = ("Courier" , 30, "bold"))
