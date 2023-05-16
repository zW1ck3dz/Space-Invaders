"""Projet - Vérification des collisions

fait le 14/05/2023 par Jason"""

import turtle
import math
import random

def tuer(cible):
    """Replacer le cible au début au contacte avec le laser"""      
    x = random.randint(-330, 330)
    y = random.randint(200, 300)
    cible.setposition(x, y)
    
def collision(a, b):
    """Fonction qui vérifie si une collision balle-cible ou joueur-cible a lieu"""
    distance = math.sqrt((a.xcor()-b.xcor())**2 + (a.ycor()-b.ycor())**2)
    if distance < 18:
        return True
    else:
        return False   

def collisionbc(collision, etatballe):
    """Fonction qui gère une collision entre une balle et une cible"""
    if collision(balle, cible):
        # On réinitialise la balle
        balle.hideturtle()
        etatballe = "ready" # Réinitialisation de l'état de la balle pour pouvoir tirer à nouveau
        balle.setposition(0, -500)# On enlève la balle de la fenêtre pour s'assurer qu'une autre cible ne rentre pas dedans
        # On replace la cible 
        x = random.randint(-330, 330)
        y = random.randint(200, 300)
        cible.setposition(x, y)
        

def collisionjc(collision):
    """Fonction qui gère une collision entre le joueur et une cible"""
    if collision(joueur, cible):
        # On enlève tout de l'écran car la partie est finie
        joueur.hideturtle()
        cible.hideturtle()
        # On affiche le texte "GAME OVER"
        stylo = turtle.Turtle()
        stylo.speed(0)
        stylo.color("Red")
        stylo.penup()
        stylo.setposition(0, 0)
        FIN = "GAME OVER"
        stylo.write(FIN, move = False, align = "center",
                font = ("Courier" , 72, "bold"))
        stylo.hideturtle()
     