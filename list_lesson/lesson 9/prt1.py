from mrmood import Mrmood
import turtle
gamgin =True
moo = Mrmood(False, False, False)

while gamgin:
    moo.changeangery()
    moo.changeeyes()
    moo.changesmile()
    print("This is mr mood")
    print("1: make him frown")
    print("2: make him angry")
    print("3: make chnge the eyes to blue")
    print("0: quit")
    change = input("what would you like to change? ")
    if change == "1":
        turtle.clear()
        moo.changesmile()
        moo.smile = not moo.smile
    elif change == "2":
        turtle.clear()
        moo.changeangery()
        moo.ntangery = not moo.smile
    elif change == "3":
        turtle.clear()
        moo.changeeyes()
        moo.eyes = not moo.eyes
    elif change == "0":
        gamgin = False
    else:
        print("bad read try again")
