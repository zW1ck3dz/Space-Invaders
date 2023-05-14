""" Space Invaders - Création des personnages de jeu

fait le ... par Lucas """

import turtle
import random

def joueur():
    """Création du héros"""
    hero = turtle.Turtle()
    turtle.register_shape("hero.gif")
    hero.shape("hero.gif")
    hero.penup()
    hero.speed(0)
    hero.setposition(0, -300)
    
def cibles():
    """Création de l'ensemble des cibles, et leur caractéristiques"""
    cibles = []
    nb_cibles = 7
    turtle.register_shape("cible.gif")
    
    for i in range(nb_cibles):
        cibles.append(turtle.Turtle())
        
    for cible in cibles:
        cible.shape("cible.gif")
        cible.speed(0)
        cible.penup()
        x = random.randint(-330, 330)
        y = random.randint(200, 300)
        cible.setposition(x, y)
        
        
        
    