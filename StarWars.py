import turtle


def balra():
    ship.setx(ship.xcor()-10)


def jobbra():
    ship.setx(ship.xcor()+10)


def fel():
    ship.sety(ship.ycor()+10)


def le():
    ship.sety(ship.ycor()-10)


space = turtle.Screen()
space.setup(width=800,height=600)
space.bgpic("img/space.png")
space.addshape("img/sprite.gif")

space.listen()
space.tracer(0)

space.onkeypress(balra, "Left")
space.onkeypress(jobbra, "Right")
space.onkeypress(fel, "Up")
space.onkeypress(le, "Down")

ship = turtle.Turtle()
ship.shape("img/sprite.gif")

while True:

    space.update()
