""" Space Invaders - Game over

créé par Jason le 17.05.2023"""

import turtle

def game_over(cibles, hero, laser):
    """Arêter le jeu avec un message GAME OVER."""
    for cible in cibles:
                cible.hideturtle()
                
    hero.hideturtle()
    laser.hideturtle()
    stylo_fin = turtle.Turtle()
    stylo_fin.speed(0)
    stylo_fin.color("Red")
    stylo_fin.penup()
    stylo_fin.setposition(0, 0)
    FIN = "GAME OVER"
    stylo_fin.write(FIN, move = False, align = "center",
            font = ("Courier" , 72, "bold"))
    pen.hideturtle()