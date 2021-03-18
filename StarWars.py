import turtle
import time
from random import *


def balra():
    ship.setx(ship.xcor()-10)


def jobbra():
    ship.setx(ship.xcor()+10)


def fel():
    ship.sety(ship.ycor()+10)


def le():
    ship.sety(ship.ycor()-10)


def MeteorYcorSorsol():
    meteor.sety(randint(-250, 250))


space = turtle.Screen()
space.setup(width=800,height=600)
space.bgpic("img/space.png")
space.addshape("img/sprite.gif")
space.addshape("img/meteor2.gif")

space.listen()
space.tracer(0)

space.onkeypress(balra, "Left")
space.onkeypress(jobbra, "Right")
space.onkeypress(fel, "Up")
space.onkeypress(le, "Down")

meteor= turtle.Turtle()
meteor.shape("img/meteor2.gif")
meteor.penup()
meteor.setx(380)
MeteorYcorSorsol()

ship = turtle.Turtle()
ship.shape("img/sprite.gif")
ship.penup()

while True:

    if ship.xcor() > 400:
        ship.setx(-390)
    if ship.xcor() < -400:
        ship.setx(390)
    if ship.ycor() > 300:
        ship.sety(-290)
    if ship.ycor() < -300:
        ship.sety(290)
    meteor.setx(meteor.xcor()-0.3)
    if meteor.xcor() < -400:
        MeteorYcorSorsol()
        meteor.setx(380)
    space.update()
