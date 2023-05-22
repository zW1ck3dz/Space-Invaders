""" Space Invaders - fichier final

crée le 14.05.2023 par Lucas & Jason."""

from turtle import register_shape, listen, onkeypress, update, Turtle
import random

from environnement_de_jeu import fenetre, bords
from mouvement_heros import gauche, droit
from collisions import tuer
from game_over import fin, relancer


# Mise en place de l'environement de jeu (écrit par Lucas et légèrement modifié par Jason)
fenetre()
bords()


# Mise en place du score initial (Jason)
S = 0

# Stylo qui écrira le score
stylo_score = Turtle()
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
hero = Turtle()
register_shape("hero.gif")
hero.shape("hero.gif")
hero.penup()
hero.speed(0)
hero.setposition(0, -300)


# Stylo qui "dessinera" le laser
laser = Turtle()
register_shape("laser.gif")
laser.shape("laser.gif")
laser.penup()
laser.hideturtle()
laser.speed(0)
laser.setposition(hero.xcor(), hero.ycor() + 35)
laser.showturtle()


# Les cibles
cibles = []
NB_CIBLES = 10
VITESSE_CIBLE = 1.8
register_shape("cible.gif")

for i in range(NB_CIBLES):
    cibles.append(Turtle())

for cible in cibles:
    cible.shape("cible.gif")
    cible.speed(0)
    cible.penup()
    coordonnee_x = random.randint(-300, 300)
    coordonnee_y = random.randint(200, 300)
    cible.setposition(coordonnee_x, coordonnee_y)


# Des fonctions qui feront bouger le héros
# à droite ou à gauche en fonction de la touche appuyée par l'utilisateur
listen()
onkeypress(lambda: gauche(hero), "Left")
onkeypress(lambda: droit(hero), "Right")


# Boucle de jeu principal
while True:
    # Affichage du score
    stylo_score.clear()
    SCORE = AFFICHE.format(S)
    stylo_score.write(SCORE, move = False, align = "center",
        font = ("Courier" , 30, "bold"))


    # Définition de la vitesse et du mouvement du laser
    V_LASER = 30
    y_laser = laser.ycor()
    y_laser += V_LASER
    laser.sety(y_laser)
    if y_laser > 350:
        laser.hideturtle()
        laser.setposition(hero.xcor(), hero.ycor() + 35)
        laser.showturtle()


    # Mouvement des cibles (écrit par Jason et implémenté par Lucas)
    for cible in cibles:
        coordonnee_x = cible.xcor()
        coordonnee_x += VITESSE_CIBLE
        cible.setx(coordonnee_x)
        # Le changement de direction quand une cible arrive à un bord
        if cible.xcor() > 330 or cible.xcor() < -330:
            # Assurer que TOUT les ennemis bougent
            for cible in cibles:
                coordonnee_y = cible.ycor()
                coordonnee_y -= 54
                cible.sety(coordonnee_y)
            # Inversion de la vitesse pour changer de direction
            VITESSE_CIBLE *= -1
        # Vérification d'une collision entre le laser et une cible
        elif ((cible.xcor() - 14) <= laser.xcor() <= (cible.xcor() + 14)
                and (cible.ycor() - 14) <= laser.ycor() <= (cible.ycor() + 14)):
            laser.setposition(hero.xcor(), hero.ycor() + 35)
            tuer(cible)
            S += 1
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


    # Mise à jour de la fenêtre à chaque fois
    # que la boucle est éxécutée
    update()
