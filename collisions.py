"""Projet - Vérification des collisions

fait le 16/05/2023 par Jason"""

import random


def tuer(cible):
    """ Fonction qui replace la cible lors d'un contacte laser-cible """      
    coordonnee_x = random.randint(-330, 330)
    coordonnee_y = random.randint(200, 300)
    cible.setposition(coordonnee_x, coordonnee_y)


def contact_laser_cible(cible, laser, heros, tuer, score):
    """ Fonction qui vérifie si une collision
        entre le laser et une cible a lieu """
    if ((cible.xcor() - 14) <= laser.xcor() <= (cible.xcor() + 14)
                and (cible.ycor() - 14) <= laser.ycor() <= (cible.ycor() + 14)):
        laser.setposition(heros.xcor(), heros.ycor() + 35)
        tuer(cible)
        score += 1


def contact_cible_heros(cible, heros, laser, cibles, fin, relancer, mort, rejouer):
    """ Fonction qui vérifie si une des cibles est arrivée à la même
        hauteur que le joueur et si oui, finit la partie """
    if (cible.ycor() - 12) < (heros.ycor() + 35):
        heros.hideturtle()
        laser.hideturtle()
        for ennemi in cibles:
            ennemi.hideturtle()
        # Message de fin de partie
        fin(mort)
        # Message pour comment rejouer
        relancer(rejouer)
