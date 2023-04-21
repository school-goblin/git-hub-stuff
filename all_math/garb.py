import all_math.methA as ma
import all_math.bigguymath as bigguy
from all_math.methA import *
from bigguymath import *
from triger import *
gameing = True
print(ma.add(1,1))
while gameing:

    whatdo = input("what do you want to do gamer?")
    if whatdo == "add":
        left = int(input("what do you want left?"))
        right = int(input("what do you want right?"))
        print(ma.add(left, right))
        bigguy.bigsmart(int(input("how many")))
        cont = input("agian???")
    elif whatdo == "sub":
        left = int(input("what do you want left?"))
        right = int(input("what do you want right?"))
        print(ma.sub(left, right))
        bigguy.bigsmart(int(input("how many")))
        cont = input("agian???")
    elif whatdo == "mult":
        left = int(input("what do you want left?"))
        right = int(input("what do you want right?"))
        print(ma.mult(left, right))
        bigguy.bigsmart(int(input("how many")))
        cont = input("agian???")
    elif whatdo == "div":
        left = int(input("what do you want left?"))
        right = int(input("what do you want right?"))
        print(ma.div(left, right))
        bigguy.bigsmart(int(input("how many")))
        cont = input("agian???")
    if cont == "no":
        gameing = False
    else:
        break
    print(constants["name"])

    print(sin(90))