<<<<<<< HEAD
""" Projet - Fin d'une partie

fait le 17/05/2023 par Jason"""

import turtle


def fin(x):
    """ Fonction qui affiche le message
    'GAME OVER' à la fin d'une partie """
=======
""" Space Invaders - Game over

créé par Jason le 17.05.2023"""

import turtle

def game_over(cibles, hero, laser):
    """Arêter le jeu avec un message GAME OVER."""
    for cible in cibles:
                cible.hideturtle()
                
    hero.hideturtle()
    laser.hideturtle()
>>>>>>> b09335e794080ae03948b52a237e116ecbe8ca3f
    stylo_fin = turtle.Turtle()
    stylo_fin.speed(0)
    stylo_fin.color("Red")
    stylo_fin.penup()
<<<<<<< HEAD
    stylo_fin.hideturtle()
    stylo_fin.goto(0, 0)
    stylo_fin.write(x, move = False, align = "center",
                    font = ("Courier" , 72, "bold"))
    stylo_fin.hideturtle()

def relancer(x):
    """ Fonction qui explique comment relancer une nouvelle partie """
    stylo_rejouer = turtle.Turtle()
    stylo_rejouer.speed(0)
    stylo_rejouer.color("Yellow")
    stylo_rejouer.penup()
    stylo_rejouer.hideturtle()
    stylo_rejouer.goto(0, -50)
    stylo_rejouer.write(x, move=False, align = "center",
                        font = ("Courier", 22, "bold"))
    stylo_rejouer.hideturtle()
=======
    stylo_fin.setposition(0, 0)
    FIN = "GAME OVER"
    stylo_fin.write(FIN, move = False, align = "center",
            font = ("Courier" , 72, "bold"))
    pen.hideturtle()
>>>>>>> b09335e794080ae03948b52a237e116ecbe8ca3f
