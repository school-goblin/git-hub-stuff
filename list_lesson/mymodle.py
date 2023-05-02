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
