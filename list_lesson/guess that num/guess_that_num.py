game = True
tries = 0
import random as rand

num = rand.randint(1,100)

f = open("./high_scores.txt", "w")
f.write("high score: gamer 7 tries")
f.close()

#open and read the file after the appending:
f = open("./high_scores.txt", "r")
print(f.read())


def intput(words):
    return int(input(words))

name = input("plese input your name: ")

while game:
    geuss = intput("geuss a number betwween 1 and 100: ")
    tries += 1
    if geuss == num:
        print("you win")
        print("you did it in " + str(tries) + " tries!")
        f = open("./high_scores.txt", "a")
        f.write("\nhigh score: " + name + " " + str(tries) + " tries")
        f.close()
        f = open("./high_scores.txt", "r")
        print("new score list: ")
        h = f.readline()
        while h != "":
            print(h)
            h = f.readline()
        
        f.close()
    elif geuss > num:
        print("your number is too big")
    elif geuss < num:
        print("your number is too small")
    else:
        print("hmmmmm")
    