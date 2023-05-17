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
        
        
    
    
    

    

        





