import turtle as tur
import random as ran

count = 0

def setup():
    tur.screensize(1000,800)
    tur.speed(0)

def drawRectanglePattern(centerX, centerY, offset, width, height,
count, rotation, andrewtate, curenthead):
    andrewtate = 360 / count
    
    for i in range(count):
        tur.goto(centerX, centerY)
        tur.setheading(curenthead)
        tur.fillcolor(setRandomColor())
        tur.up()
        tur.forward(offset)
        tur.left(rotation)
        tur.down()
        tur.begin_fill()
        tur.forward(width)
        tur.right(90)
        tur.forward(height)
        tur.right(90)
        tur.forward(width)
        tur.right(90)
        tur.forward(height)
        tur.end_fill()
        tur.up()
        curenthead += andrewtate
        print(curenthead)
        

        
    
        



def drawCirclePattern(centerX, centerY, offset, radius, count, andrewtate, curenthead):
    
    
    for i in range(count):
        tur.goto(centerX, centerY)
        tur.setheading(curenthead)
        tur.fillcolor(setRandomColor())
        tur.up()
        tur.forward(offset)
        tur.down()
        tur.begin_fill()
        tur.circle(radius)
        tur.end_fill()
        tur.up()
        curenthead += andrewtate
        print(curenthead)
        

def setRandomColor():
        colorNum = randint(1,4)
        if colorNum == 1:
            color = "Blue"
        elif colorNum == 2:
            color = "Green"
        elif colorNum == 3:
            color = "Red"
        else:
            color = "Black"
        return color

def drawSuperPattern(count, andrewtate):
    curenthead = 0
    for i in range(count):
        tur.up()
        recirc = randint(1,2)
        if recirc == 1:
            drawCirclePattern(randint(0, 100), randint(0,100), randint(0,200), randint(1,100),1, andrewtate, curenthead)
            curenthead += andrewtate
        elif recirc == 2:
           drawRectanglePattern(randint(0, 100), randint(0,100), randint(0,200), randint(1,100), randint(1,100),1, randint(0,360), andrewtate, curenthead)
           curenthead += andrewtate

def done():
    tur.bye()


def reset():
    tur.clear()
    print("screen cleared")

def intput(text):
    return int(input(text))

def floatput(text):
    return float(input(text))

def strput(text):
    return str(input(text))

def randint(int1, int2):
    return ran.randint(int1, int2)
    