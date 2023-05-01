numbers = [1, 2, 3, 4, 5]
print(numbers)

blueberry = "blueberry"
fruits = ["apple", "orange", "banana", blueberry]
print(fruits)

print(fruits[0])

sum = numbers[0] + numbers[1] + numbers[2]
print(sum)

print(numbers[1:4])

print("Lenght of number pre - " + str(len(numbers)))

for i in range(6, 10):
    print(i)
    numbers.append(i)

print(numbers)

print("Lenght of number post - " + str(len(numbers)))

floatlist = [89.98, 99.99, 100.00, 32.50, 11.22]


print(str(floatlist))

listlist = [floatlist, numbers, fruits ]

print(listlist)

def average(listOfNumbers):
    avg = 0
    total = 0
    loop = int(len(listOfNumbers))
    for i in range(loop):
        total += listOfNumbers[i]
    avg = total / i
    return avg

print(average(numbers))

def print_vertically(mystring):
    for index in range(0, len(mystring)):
        sting = mystring[index]
        print(sting)

print_vertically(fruits)

def replace(toFind, replaceWith, sentence):
    newStr = ""
    print(range(0, len(sentence)))
    for index in range(0, len(sentence)):
        if sentence[index] == toFind:
            newStr += replaceWith
        else:
            newStr += sentence[index]
    return newStr
       
newSentence = replace("t", "T", "the tinny tutle talks to tim")
print(newSentence)

print()
print()
print()
print()

print(floatlist)

print(floatlist)

def removeLowest(listOfNumbers):
    coolNum = listOfNumbers[0]
    for num in listOfNumbers:
        if coolNum > num:
            coolNum = num
    print("removing " + str(coolNum))
    listOfNumbers.remove(coolNum)

def deletIndesFromList(index, list):
    print("Deleting index " + str())

removeLowest(floatlist)

floatlist.sort(reverse=False)
print(floatlist)
        
def explainTheSort(list, isReverse = False):
    print(list)
    print("that was your list")
    if isReverse == False:
        print("your list is about to be reverst")
        list.sort(reverse = True)
        print(list)
    else:
        print("your list is about to be sorted not reverst")
        list.sort(reverse = False)
        print(list)


explainTheSort(floatlist, True)