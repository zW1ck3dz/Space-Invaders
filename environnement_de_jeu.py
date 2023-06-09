""" Space Invaders - Création de l'environnement de jeu

Créé le 14/05/2023 par Lucas et modifié par Jason le 16/05/2023 """

import turtle


def fenetre():
    """ Fonction qui crée la fenêtre de jeu """
    fn_jeu = turtle.Screen()
    fn_jeu.setup(width = 1000, height = 1000)
    fn_jeu.bgpic("background.gif")
    fn_jeu.title("Space Invaders")
    fn_jeu.tracer(0)


def bords():
    """ Fonction qui trace les bords de l'espace virtuelle du jeu """
    stylo_bord = turtle.Turtle()
    stylo_bord.speed(0) # vitesse de déplacement du stylo mise au max
    stylo_bord.color("lime green")
    stylo_bord.up() # tant que le stylo se déplace vers le point de départ
                    # de traçage, il est "up" donc il ne trace rien
    stylo_bord.setposition(-350, -350)
    stylo_bord.down() # le stylo est "down", comme posé sur du papier, donc peut tracer
    stylo_bord.pensize(3)
    stylo_bord.hideturtle() # on cache le stylo

    stylo_bord.forward(700)
    stylo_bord.left(90) # angle de changement de direction (on veut un carré)
    stylo_bord.forward(700)
    stylo_bord.left(90) # angle de changement de direction (on veut un carré)
    stylo_bord.forward(700)
    stylo_bord.left(90) # angle de changement de direction (on veut un carré)
    stylo_bord.forward(700)
    stylo_bord.left(90) # angle de changement de direction (on veut un carré)
