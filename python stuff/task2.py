import turtle

tutX = int(input("what do you want the X cord to be? "))
tutY = int(input("what do you want the Y cord to be? "))
tutDiam = int(input("what do you want the diamierter to be? "))
tutRad = tutDiam / 2

turtle.speed(1)
turtle.penup()
turtle.goto(tutX, tutY)
turtle.fillcolor("black")
turtle.begin_fill()
turtle.pendown()
turtle.circle(tutRad * 4)
turtle.end_fill()
turtle.penup()
turtle.lt(90)
turtle.forward(tutRad)
turtle.rt(90)
turtle.fillcolor("blue")
turtle.begin_fill()
turtle.pendown()
turtle.circle(tutRad * 3)
turtle.end_fill()
turtle.penup()
turtle.lt(90)
turtle.forward(tutRad)
turtle.rt(90)
turtle.fillcolor("red")
turtle.begin_fill()
turtle.pendown()
turtle.circle(tutRad * 2)
turtle.end_fill()
turtle.penup()
turtle.lt(90)
turtle.forward(tutRad)
turtle.rt(90)
turtle.fillcolor("yellow")
turtle.begin_fill()
turtle.pendown()
turtle.circle(tutRad * 1)
turtle.end_fill()
input()