#no
#no
import mymodle 


groceries = []
clothes = []
Electronics = []
books = []
gaming = True

while gaming:
    mymodle.liststate()
    add2list = input("do you want to add to the lists? ")
    if add2list == "yes" or add2list == "y":
        listselect = True
        witchlist = input("witch list do you want to edit? ")
        while listselect:
            if witchlist == "groceries":
                mymodle.groce()
                listselect = False
            elif witchlist == "clothes":
                mymodle.cloth()
                listselect = False
            elif witchlist == "electronics":
                mymodle.elec()
                listselect = False
            elif witchlist == "books":
                mymodle.book()
                listselect = False
            else:
                print("bad read plz try again")
    else:
        while True:
            print("")
            print("you final lists are as follows: ")
            mymodle.liststate()
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