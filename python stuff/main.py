def addOne(num):
    return(num + 2)
def printSomething(something):
    print(something)
def concatTo5(toConcat):
    return str(5) + toConcat
def twoParamFunc(one, two):
    return one + two
def main():
    number = 100
    print(addOne(1))
    theReturn = addOne(13)
    print(theReturn)
    printSomething(addOne(number))
    print(concatTo5("This is 5."))
    print(twoParamFunc(number, number + 5))
    print(twoParamFunc("one", "two"))

main()