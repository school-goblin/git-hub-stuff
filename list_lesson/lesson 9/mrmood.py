import turtle as t

#this is the guy
class Mrmood:
    blkeyes = True
    smile = True
    ntangery = True

    #my constructor
    def __init__(self, eyes, smile, angery):
        self.eyes = eyes
        self.smile = smile
        self.ntangery = angery


    #this will redraw the smile
    def changesmile(self):
        if self.smile == True:
            #draw frown
            t.home()
            t.pencolor("black")
            t.penup()
            t.goto(35, 0)
            t.pendown()
            t.pensize(5)
            t.left(90)
            t.circle(40, 125)
            t.penup()

        
        elif self.smile == False:
            #draw smile
            t.home()
            t.pencolor("black")
            t.penup()
            t.goto(25, 25)
            t.pendown()
            t.pensize(5)
            t.right(315)
            t.circle(40, -120)
            t.penup()


    def changeeyes(self):
        if self.eyes == True:
            #draw eyes blue
            t.home()
            t.penup()
            t.goto(-25,45)
            t.fillcolor("blue")
            t.begin_fill()
            t.circle(10)
            t.end_fill()
            t.penup()
            t.goto(25,45)
            t.begin_fill()
            t.circle(10)
            t.end_fill()
            t.penup()
            
    

        elif self.eyes == False:
            #draw eyes Black
            t.home()
            t.penup()
            t.goto(-25,45)
            t.fillcolor("black")
            t.begin_fill()
            t.circle(10)
            t.end_fill()
            t.penup()
            t.goto(25,45)
            t.begin_fill()
            t.circle(10)
            t.end_fill()
            t.penup()

    def changeangery(self):
        if self.ntangery == True:
            #draw red
            t.color("red")
            t.home()
            t.penup()
            t.goto(0, 0)
            t.fillcolor("red")
            t.begin_fill()
            t.circle(50)
            t.end_fill()
            t.penup()
      
            
        elif self.ntangery == False:
            #draw yellow
            t.home()
            t.color("yellow")
            t.fillcolor("yellow")
            t.begin_fill()
            t.circle(50)
            t.end_fill()
            t.penup()
          