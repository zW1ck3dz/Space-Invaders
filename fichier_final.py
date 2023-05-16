""" Space Invaders - fichier final

crée le 14.05.2023 par Lucas."""

import turtle
import random

from environnement_de_jeu import fenetre, bords
from tirer_le_laser import tirer
from bouger_héro import gauche, droit
from collisions import tuer, collision, collisionbc, collisionhc
from final_score import score, AFFICHE, s, point

# Mise en place de l'environement de jeu (écrit par Lucas et légèrement modifié par Jason)
fn = turtle.Screen()
fn.setup(width = 1000, height = 1000)
fn.bgpic("background.gif")
fn.title("Space Invaders")
fn.tracer(0) #rend le jeu "smooth"
bords()
    
# Affichage du score (Jason)
score(s)
    
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

def tirer(hero, laser):
    laser.showturtle()
    x_laser = hero.xcor()
    y_laser = hero.ycor() + 35
    laser.setposition(x_laser, y_laser)
    laser.showturtle()
    
    v_laser = 30
    
    while laser.ycor() < 350:
        y_laser += v_laser
        laser.sety(y_laser)
        
    laser.hideturtle()
    
# Les cibles
cibles = []
nb_cibles = 7
vitessecible = 1.8
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
                
                
turtle.listen()
turtle.onkeypress(lambda: tirer(hero, laser), "space")
turtle.onkeypress(lambda: gauche(hero), "Left")
turtle.onkeypress(lambda: droit(hero), "Right")

# Boucle de jeu principal 
while True:
    
    fn.update()
    # Mouvement des cibles (écrit par Jason et implémenté par Lucas)
    for cible in cibles:
        x = cible.xcor()
        x += vitessecible
        cible.setx(x)
        
        # Le changement de direction quand une cible arrive à un bord
        if cible.xcor() > 330 or cible.xcor() < -330:
            # Assurer que TOUT les ennemis bougent
            for cible in cibles:
                y = cible.ycor()
                y -= 54
                cible.sety(y)
            # Inversion de la vitesse pour changer de direction
            vitessecible *= -1.1
            
        if (cible.xcor() - 12) <= laser.xcor() <= (cible.ycor() + 12) and (cible.ycor() - 12) <= laser.ycor() <= (cible.ycor() + 12):
            tuer(cible)
            laser.hideturtle()
            
        if collision(laser, cible):
            # On réinitialise la balle
            balle.hideturtle()
            #etatballe = "ready" # Réinitialisation de l'état de la balle pour pouvoir tirer à nouveau
            balle.setposition(0, -500)# On enlève la balle de la fenêtre pour s'assurer qu'une autre cible ne rentre pas dedans
            # On replace la cible 
            x = random.randint(-330, 330)
            y = random.randint(200, 300)
            cible.setposition(0, 10000)
            point(s)
        
        if collision(hero, cible):
            # On enlève tout de l'écran car la partie est finie
            hero.hideturtle()
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

    
   
        
        
    
    
    

    

        





