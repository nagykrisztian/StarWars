import turtle
import time
from random import *
import winsound


def balra():
    ship.setx(ship.xcor()-10)


def jobbra():
    ship.setx(ship.xcor()+10)


def fel():
    ship.sety(ship.ycor()+10)


def le():
    ship.sety(ship.ycor()-10)


def MeteorYcorSorsol(meteor, index):
    meteor.sety(randint(-250, 250))
    meteor.setx(380+index*50)


def MeteorGeneralas(index):
    meteor_lista.append(turtle.Turtle())
    meteor_lista[index].shape("img/meteor2.gif")
    meteor_lista[index].penup()
    MeteorYcorSorsol(meteor_lista[index], index)

eleteropont = 3

space = turtle.Screen()
space.setup(width=800,height=600)
space.bgpic("img/background.png")
space.addshape("img/sprite.gif")
space.addshape("img/meteor2.gif")

space.listen()
space.tracer(0)

space.onkeypress(balra, "Left")
space.onkeypress(jobbra, "Right")
space.onkeypress(fel, "Up")
space.onkeypress(le, "Down")


ship = turtle.Turtle()
ship.shape("img/sprite.gif")
ship.penup()

meteor_lista = []
for x in range(0,3):
    MeteorGeneralas(x)

kijelzo = turtle.Turtle()
kijelzo.color("white")
kijelzo.hideturtle()
kijelzo.penup()
kijelzo.sety(240)
kijelzo.setx(-380)
kijelzo.write(f"Életerő: {eleteropont}",font=("Arial", 30, "bold"))

while True:

    if ship.xcor() > 400:
        ship.setx(-390)
    
    if ship.xcor() < -400:
        ship.setx(390)
    
    if ship.ycor() > 300:
        ship.sety(-290)
    
    if ship.ycor() < -300:
        ship.sety(290)
    
    for x in meteor_lista:
        x.setx(x.xcor()-0.3)
        if x.xcor() < -400:
            MeteorYcorSorsol(x, meteor_lista.index(x))
        if ship.distance(x.xcor(), x.ycor()) < 35:
            winsound.PlaySound("sound/explosion-01.wav", winsound.SND_ASYNC)
            eleteropont-=1
            kijelzo.clear()
            kijelzo.write(f"Életerő: {eleteropont}",font=("Arial", 30, "bold"))
            MeteorYcorSorsol(x, meteor_lista.index(x))
    
    if eleteropont == 0:
        kijelzo.clear()
        kijelzo.sety(0)
        kijelzo.setx(0)
        kijelzo.write("Game over",align="center",font=("Arial", 40, "bold"))
        ship.hideturtle()
        for x in meteor_lista:
            x.hideturtle()
        meteor_lista.clear()
    
    space.update()
