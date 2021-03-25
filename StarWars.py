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
        if ship.distance(x.xcor(), x.ycor()) < 20:
            winsound.PlaySound("sound/explosion-01.wav", winsound.SND_ASYNC)
            MeteorYcorSorsol(x, meteor_lista.index(x))
    
    space.update()
