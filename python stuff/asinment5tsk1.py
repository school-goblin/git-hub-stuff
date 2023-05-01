# andrew saunders 3rd hour ashinment 5 task 1 :)
# i import a library beacause i need a randome num
import random
print("weolcom to the guessing game!")
print("my cool program has picked a number from 1-10")
#gets input (i am aware i mispebled user, and no im not fixing it)
urser = int(input("what number do you choise? (1-10): "))
#gets number from the realy cool library
number = random.randint(1, 10)

#my realy cool number checker
if urser == number:
    msg = "wow right on the mony, good work"
elif urser + 1 == number or urser - 1 == number:
    msg = "close you were only one off, the number was " + str(number)
elif urser + 2 == number or urser - 2 == number:
    msg = "tsck tsck you were too off. its just sad realy. the number was " + str(number)
elif urser + 3 == number or urser - 3 == number:
    msg = "wow i had no idea how garb you are. you are problebly one of my least favorite people. the number was " + str(number)
else:
    msg = "i hate you. are you even trying. even an ape could have done better. the number was " + str(number) + " \nnow go crawl back to the hole you crawled out of"
#prints my mesage :) yay
print(msg)