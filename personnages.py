""" Space Invaders - Création des personnages de jeu

fait le ... par Lucas """

import turtle
import random

def hero():
    """Création du héros"""
    hero = turtle.Turtle()
    turtle.register_shape("hero.gif")
    hero.shape("hero.gif")
    hero.penup()
    hero.speed(0)
    hero.setposition(0, -300)
    
    x_hero = hero.xcor()
    y_hero = hero.ycor()
    
    # Mise en place du laser sans le mécanisme de tirer (autre fichier)
    laser = turtle.Turtle()
    turtle.register_shape("laser.gif")
    laser.shape("laser.gif")
    laser.penup()
#     laser.hideturtle
    laser.speed(0)
    
    x_laser = x_hero
    y_laser = y_hero + 35
    laser.setposition(x_laser, y_laser)
        
        
    
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
        
        
        
    