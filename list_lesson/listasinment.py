#no
#no

groceries = []
clothes = []
Electronics = []
books = []
gaming = True

def liststate():
    groceries.sort()
    clothes.sort()
    Electronics.sort()
    books.sort()
    print("your list: ")
    print("groceries: " + str(groceries))
    print("clothes: " + str(clothes))
    print("Electronics: " + str(Electronics))
    print("books: " + str(books))

def groce():
    groceries.append(input("what do you want to add to groceries? "))

def cloth():
    clothes.append(input("what do you want to add to clothing? "))

def elec():
    Electronics.append(input("what do you want to add to electronics? "))

def book():
    books.append(input("what do you want to add to books? "))


while gaming:
    liststate()
    add2list = input("do you want to add to the lists? ")
    if add2list == "yes" or add2list == "y":
        listselect = True
        witchlist = input("witch list do you want to edit? ")
        while listselect:
            if witchlist == "groceries":
                groce()
                listselect = False
            elif witchlist == "clothes":
                cloth()
                listselect = False
            elif witchlist == "electronics":
                elec()
                listselect = False
            elif witchlist == "books":
                book()
                listselect = False
            else:
                print("bad read plz try again")
    else:
        while True:
            print("")
            print("you final lists are as follows: ")
            liststate()
            change = input("would you like to remove anything from the list? ")
            if change == "y" or change == "yes":
                witchlist = input("whitch list would you like to remove from? ")
                goneword = input("what word would you like to remove? ")
                if witchlist == "books":
                    books.remove(goneword)
                elif witchlist == "electronics":
                    Electronics.remove(goneword)
                elif witchlist == "groceries":
                    groceries.remove(goneword)
                elif witchlist == "clothes":
                    clothes.remove(goneword)