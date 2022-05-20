import time
import turtle

okno = turtle.Screen()
okno.title("Hadík")
okno.bgcolor("#fffdd0")
okno.setup(width=600, height=600)
okno.tracer(0)

hadik = turtle.Turtle()
hadik.shape("square")
hadik.color("#ff69b4")
hadik.goto(0, 0)
hadik.direction = "stop"
hadik.penup()

jidlo = turtle.Turtle()
jidlo.shape("circle")
jidlo.color("#0080ff")
jidlo.goto(200, 200)
jidlo.direction = "stop"
jidlo.penup()

def nahoru():
    hadik.direction = "up"
def dolu():
    hadik.direction = "down"
def vlevo():
    hadik.direction = "left"
def vpravo():
    hadik.direction = "right"

def pohyb():
    if hadik.direction == "up":
        y = hadik.ycor()
        hadik.sety(y+20)
    if hadik.direction == "down":
        y = hadik.ycor()
        hadik.sety(y-20)
    if hadik.direction == "left":
        x = hadik.xcor()
        hadik.setx(x-20)
    if hadik.direction == "right":
        x = hadik.xcor()
        hadik.setx(x+20)

okno.listen()
okno.onkeypress(nahoru, "w")
okno.onkeypress(dolu, "s")
okno.onkeypress(vlevo, "a")
okno.onkeypress(vpravo, "d")

skore = 0
pero = turtle.Turtle()
pero.hideturtle()
pero.penup()
pero.goto(0, 250)
pero.write("Skóre: {}".format(skore), align="center", font=("candara", 24, "bold"))

import time
import random
while True:
    okno.update()
    if hadik.xcor() > 290 or hadik.xcor() < -290 or hadik.ycor() > 290 or hadik.ycor() < -290:
        time.sleep(1)
        hadik.goto(0,0)
        hadik.direction = "stop"
    if hadik.distance(jidlo) < 20:
        x = random.randint(-270, 270)
        y = random.randint(-270, 270)
        jidlo.goto(x, y)
        skore += 1
        pero.clear()
        pero.write("Skóre: {}".format(skore), align="center", font=("candara", 24, "bold"))
    pohyb()
    time.sleep(0.1)
# okno.mainloop()