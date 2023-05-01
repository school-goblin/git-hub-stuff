# andrew saunders 3rd hour ashinment 5 task 1 :)
# i import a library beacause i want a randome num
import random
#I import math because i atualy needd need it 
import math

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
    msg1 = str(name2) + " is in " + str(name1)
elif distance < radis2:
    msg1 = str(name1) + " is in " + str(name2)
elif distance < radis1 and radis2:
    msg1 = "they are in each other"
else:
    msg1 = "they are not in the space"

if distance > radis1 + radis2:
    msg2 = "the spaces do not overlap"
elif distance < radis1 + radis2:
    msg2 = "they overlap"
elif distance + radis1 < radis2:
    msg2 ="green is in red"
elif distance + radis2 < radis1:
    msg2 = "red is in green"    

print(distance)
print(str(msg1) + "\n" + str(msg2))




























#just in case
import turtle