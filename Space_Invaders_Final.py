""" Space Invaders - fichier final

crée le 14.05.2023 par Lucas & Jason."""

from turtle import register_shape, listen, onkeypress, update, Turtle
import random

from environnement_de_jeu import fenetre, bords
from fonctions_heros import gauche, droit, affiche_heros
from collisions import tuer
from game_over import fin, relancer
from print_score import affiche_score, point
from fonctions_laser import affiche_laser, mouvement_laser
from affichage_cibles import affiche_cibles


# Template pour le score
AFFICHE = "Score : {}"

# Mise en place du score initial & la vitesse du laser 
score = 0
V_LASER = 20

# Mise en place du nombre de cibles et leur vitesse
NB_CIBLES = 10
VITESSE_CIBLE = 2

# Templates des messages affichés à la fin d'une partie
MORT = "GAME OVER"
REJOUER = "Veuillez relancer le programme pour rejouer"


# Mise en place de l'environement de jeu 
fenetre()
bords()


# Stylo qui écrira le score
stylo_score = affiche_score()


# Stylo qui "dessinera" le héros
heros = affiche_heros()


# Stylo qui "dessinera" le laser
laser = affiche_laser(heros)


# Création des cibles
cibles = []
cible = affiche_cibles(NB_CIBLES, cibles)


# Des fonctions qui feront bouger le héros
# à droite ou à gauche en fonction de la
# touche appuyée par l'utilisateur
listen()
onkeypress(lambda: gauche(heros), "Left")
onkeypress(lambda: droit(heros), "Right")


# Boucle de jeu principal
while True:
    # Affichage du score
    point(stylo_score, AFFICHE, score)

    # Définition du mouvement du laser
    mouvement_laser(laser, heros, V_LASER)

    # Mouvement des cibles 
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
        elif ((cible.xcor() - 14) <= laser.xcor() <= (cible.xcor() + 14)
                and (cible.ycor() - 14) <= laser.ycor() <= (cible.ycor() + 14)):
            laser.setposition(heros.xcor(), heros.ycor() + 35)
            tuer(cible)
            score += 1
        elif (cible.ycor() - 12) < (heros.ycor() + 35):
            heros.hideturtle()
            laser.hideturtle()
            for cible in cibles:
                cible.hideturtle()
            # Message de fin de partie
            fin(MORT)
            # Message pour comment rejouer
            relancer(REJOUER)
            break

    # Mise à jour de la fenêtre à chaque fois
    # que la boucle est éxécutée
    update()
