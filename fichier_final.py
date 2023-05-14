""" Space Invaders - fichier final

crée le 14.05.2023 par Lucas."""

import turtle
import random

from environnement_de_jeu import fenetre, bords
from tirer_le_laser import tirer



# Mise en place de l'environement de jeu
fenetre()
bords()
    
# Affichage du score (Jason)
    
    
# Le héro
hero = turtle.Turtle()
turtle.register_shape("hero.gif")
hero.shape("hero.gif")
hero.penup()
hero.speed(0)
hero.setposition(0, -300)
    
# Le laser
laser = turtle.Turtle()
turtle.register_shape("laser.gif")
laser.shape("laser.gif")
laser.penup()
laser.hideturtle()
laser.speed(0)
        
# Les cibles
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
    

            
  

    
# Boucle de jeu principal 
while True:
    turtle.listen()
    turtle.onkeypress(lambda: tirer(hero, laser), "space")
    
    
    
    
    
    
    
    turtle.update()
        
        
    
    
    

    

        





