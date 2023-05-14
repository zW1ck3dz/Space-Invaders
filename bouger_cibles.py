"""Projet - Bouger les cibles

fait le 14/05/2023 par Jason"""


def bougercibles(cible):
    """Cette fonction sert à faire bouger les cibles"""
    #Bouger les cibles
    for cible in cibles:
        x = cible.xcor()
        x += vitessecible
        cible.setx(x)
        
        #Le changement de direction quand une cible arrive au bord DROIT de l'écran
        if cible.xcor() > 330:
            #Assurer que TOUT les ennemis bougent
            for cible in cibles:
                y = cible.ycor()
                y -= 54
                cible.sety(y)
            #Inversion de la vitesse pour changer de direction
            vitessecible *= -1

        #Le changement de direction quand une cible arrive au bord GAUCHE de l'écran
        if cible.xcor() < -330:
            #Assurer que TOUT les ennemis bougent
            for cible in cibles:
                y = cible.ycor()
                y -= 54
                cible.sety(y)
            #Inversion de la vitesse pour changer de direction
            vitessecible *= -1