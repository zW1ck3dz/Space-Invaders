""" Space Invaders - Création de l'environnement de jeu

Créé le ... par Lucas """

import turtle


def fenetre():
    """ Fonction qui crée la fenêtre de jeu """
    fn = turtle.Screen()
    fn.setup(width = 1000, height = 1000)
    fn.bgpic("background.gif")
    fn.title("Space Invaders")
    fn.tracer(0)


def bords():
    """ Fonction qui trace les bords de l'espace virtuelle du jeu """
    stylo_bord = turtle.Turtle()
    stylo_bord.speed(0) # vitesse de déplacement du stylo mise au max 
    stylo_bord.color("lime green")
    stylo_bord.up() # tant que le stylo se déplace vers le point de départ de traçage, elle est "up", donc ne trace rien
    stylo_bord.setposition(-350, -350)
    stylo_bord.down() # le stylo est "down", comme posé sur du papier, donc peut tracer
    stylo_bord.pensize(3)
    stylo_bord.hideturtle() # on cache le stylo

    for i in range(4):
        stylo_bord.forward(700)
        stylo_bord.left(90) # angle de changement de direction (on veut un carré)
    






