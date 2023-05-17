<<<<<<< HEAD:fichier_final.py
""" Space Invaders - fichier final

crée le 14.05.2023 par Lucas."""

import turtle
import random

from environnement_de_jeu import fenetre, bords
from bouger_héro import gauche, droit
from collisions import tuer
from game_over import fin, relancer


# Mise en place de l'environement de jeu (écrit par Lucas et légèrement modifié par Jason)
fenetre()
bords()


# Mise en place du score initial (Jason)
s = 0

# Stylo qui écrira le score
stylo_score = turtle.Turtle()
stylo_score.speed(0)
stylo_score.color("Lime")
stylo_score.penup()
stylo_score.hideturtle()
stylo_score.goto(0, 400)

# Template pour le score
AFFICHE = "Score : {}"


# Templates des messages affichés à la fin d'une partie
MORT = "GAME OVER"
REJOUER = "Veuillez relancer le programme pour rejouer"


# Stylo qui "dessinera" le héros
hero = turtle.Turtle()
turtle.register_shape("hero.gif")
hero.shape("hero.gif")
hero.penup()
hero.speed(0)
hero.setposition(0, -300)
    
    
# Stylo qui "dessinera" le laser
laser = turtle.Turtle()
turtle.register_shape("laser.gif")
laser.shape("laser.gif")
laser.penup()
laser.hideturtle()
laser.speed(0)
laser.setposition(hero.xcor(), hero.ycor() + 35)
laser.showturtle()


# Les cibles
cibles = []
nb_cibles = 10
vitessecible = 2
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
                

# Des fonctions qui feront bouger le héros
# à droite ou à gauche en fonction de la touche appuyée par l'utilisateur
turtle.listen()
turtle.onkeypress(lambda: gauche(hero), "Left")
turtle.onkeypress(lambda: droit(hero), "Right")


# Boucle de jeu principal 
while True:
    # Affichage du score
    stylo_score.clear()
    SCORE = AFFICHE.format(s)
    stylo_score.write(SCORE, move = False, align = "center",
        font = ("Courier" , 30, "bold"))

    
    # Définition de la vitesse et du mouvement du laser
    v_laser = 30
    y_laser = laser.ycor()
    y_laser += v_laser
    laser.sety(y_laser)
    if y_laser > 350:
        laser.hideturtle()
        laser.setposition(hero.xcor(), hero.ycor() + 35)
        laser.showturtle()
        
    
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
            vitessecible *= -1
        # Vérification d'une collision entre le laser et une cible
        elif ((cible.xcor() - 12) <= laser.xcor() <= (cible.xcor() + 12)
                and (cible.ycor() - 12) <= laser.ycor() <= (cible.ycor() + 12)):
            laser.setposition(hero.xcor(), hero.ycor() + 35)
            tuer(cible)
            s += 1
        # On vérifie si une des cibles est arrivée à la même
        # hauteur que le joueur et si oui, la partie se finit
        elif (cible.ycor() - 12) < (hero.ycor() + 35):
            hero.hideturtle()
            laser.hideturtle()
            for cible in cibles:
                cible.hideturtle()
            # Message de fin de partie
            fin(MORT)
            # Message pour comment rejouer
            relancer(REJOUER)
            break # On quitte la boucle de jeu


    
    turtle.update()


    
=======
""" Space Invaders - fichier final

crée le 14.05.2023 par Lucas."""

import turtle
import random

from environnement_de_jeu import fenetre, bords
from bouger_héro import gauche, droit
from collisions import tuer
from game_over import game_over

# Mise en place de l'environement de jeu
fn = fenetre()
bords()
    
# Définition du score
s = 0
AFFICHE = "Score : {}"
stylo_score = turtle.Turtle()
stylo_score.speed(0)
stylo_score.color("Lime")
stylo_score.penup()
stylo_score.hideturtle()
stylo_score.goto(0, 400)  
    
# Le héro
hero = turtle.Turtle()
turtle.register_shape("hero.gif")
hero.shape("hero.gif")
hero.penup()
hero.speed(0)
hero.setposition(0, -300)
    
# Le laser
laser = turtle.Turtle()
laser.hideturtle()
laser.speed(0)
turtle.register_shape("laser.gif")
laser.shape("laser.gif")
laser.penup()
laser.setposition(hero.xcor(), hero.ycor() + 35)
laser.showturtle()
v_laser = 2

# Les cibles
cibles = []
nb_cibles = 7
vitessecible = 0.1
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
turtle.onkeypress(lambda: gauche(hero), "Left")
turtle.onkeypress(lambda: droit(hero), "Right")

# Boucle de jeu principal 
while True:
    
    # Affichage du score
    stylo_score.clear()
    SCORE = AFFICHE.format(s)
    stylo_score.write(SCORE, move = False, align = "center",
        font = ("Courier" , 30, "bold"))
    
    
    # Mouvement constant du laser
    y_laser = laser.ycor()
    y_laser += v_laser
    laser.sety(y_laser)
    
    if y_laser > 350:
        laser.setposition(hero.xcor(), hero.ycor() + 35)
    
    
    # Mouvement des cibles (écrit par Jason et implémenté par Lucas)
    for cible in cibles:
        x = cible.xcor()
        x += vitessecible
        cible.setx(x)
        
        # Le changement de direction quand une cible arrive à un bord
        if cible.xcor() > 330 or cible.xcor() < -330:
            # Assurer que TOUS les ennemis bougent
            for cible in cibles:
                y = cible.ycor()
                y -= 54
                cible.sety(y)
            # Inversion de la vitesse pour changer de direction
            vitessecible *= -1
            
        if (cible.xcor() - 12) <= laser.xcor() <= (cible.xcor() + 12) and (cible.ycor() - 12) <= laser.ycor() <= (cible.ycor() + 12):
            laser.setposition(hero.xcor(), hero.ycor() + 35)
            tuer(cible)
            s += 1
        
        if (cible.ycor() - 12) < (hero.ycor() + 35):
            game_over(cibles, hero, laser)
            break
        
    

    turtle.update()
    fn.update()
        
        
    
    
    

    

        





>>>>>>> b09335e794080ae03948b52a237e116ecbe8ca3f:Space_Invaders_Final.py
