# andrew saunders 3rd hour ashinment 5 task 1 :)
# i import a library beacause i want a randome num
import random
#I import math because i atualy needd need it 
import math
import turtle
#yay now i have a nuber :)
andrews_personal_number = random.randint(1, 1000000000000000000000000000000000)

print("Welcome to the Social Situation Analyzer System")

print("Person One")
name1 = input("Enter your name: ")
onex = int(input("Enter your position (x): "))
oney = int(input("Enter your position (y): "))

radis1 = int(input("Enter your personal space radius: "))

print("Person Two")
name2 = input("Enter your name: ")
twox = int(input("Enter your position (x): "))
twoy = int(input("Enter your position (y): "))

radis2 = int(input("Enter your personal space radius: "))

disY = (oney - twoy) ** 2
disX = (onex - twox) ** 2 
distance = math.sqrt( disX + disY )



if distance < radis1:
    print("one is in two")
elif distance < radis2:
    print("two is in one")
elif distance < radis1 and radis2:
    print("they are in each other")
else:
    print("they are not in the space")

if distance > radis1 + radis2:
    print("the spaces do not overlap")
elif distance + radis1 < radis2:
    print("red is in green")
elif distance + radis2 < radis1:
    print("green is in red")    

print(distance)

turtle.speed(1)
turtle.penup()
turtle.goto(onex, oney)
turtle.pendown()
turtle.fillcolor("red")
turtle.begin_fill()
turtle.circle(radis1)
turtle.end_fill()
turtle.penup()
turtle.goto(twox, twoy)
turtle.pendown()
turtle.fillcolor("green")
turtle.begin_fill()
turtle.circle(radis2)
turtle.end_fill()
turtle.penup()
turtle.goto(1000, 1000)
input()