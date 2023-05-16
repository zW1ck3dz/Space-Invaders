""" Space Invaders - Création du laser

fait le 14.05.2023 par Lucas """

import turtle
import time

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
        laser.sety(y)
      
    laser.hideturtle()

        

    
    