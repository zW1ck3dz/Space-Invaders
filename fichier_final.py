""" Space Invaders - fichier final

crée le 14.05.2023 par Lucas."""

from environnement_de_jeu import fenetre, bords
from personnages import hero, cibles
from creation_laser import laser


def jeu_final:
    """ Rassemble tous les fichiers composants du jeu """
    fenetre()
    bords()
    hero()
    cibles()
    
    # Boucle de jeu
    while True:
        





