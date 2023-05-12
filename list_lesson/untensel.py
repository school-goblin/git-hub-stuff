class Untensil: 
    type  = "spoon"
    material = "plastic"

    def __init__(self, type, material):
        self.type = type
        self.material = material

    def cut(self):
        if self.type == "knife":
            print("I am a knife, I will cut you.")
        elif self.type == "fork":
            print("I am fork, I can try to cut.")
        elif self.type == "spork":
            print("i can cut, not bragin though")
        else:
            print("I am not something thats suposed to cut")
    
    def liftfood(self):
        if self.type == "fork":
            print("i lift the food by stabing it repdidly over and over and over and over and over again.")
        elif self.type == "spoon":
            print("i scoup and then you sipp the soup becase im a spoon")
        elif self.type == "spork":
            print("I can cut and scoupe and lift, i am the best ever")
        else:
            print("ima knife, i dont lift. stupid")

class Person:
    type = "based"
    maerial = "flesh"
    race = "and im going to win"
    music = "chill"
    age = 18
    __name = "None"

    def __init__(self, type, material, race):
        self.type = type
        self.maerial = material
        self.race = race

    def breath(self):
        if self.maerial == "flesh":
            print("*breath in*")
            print("*breath out*")
        else:
            print("*intence gasping*")
        
    def speak(self):
        if self.type == "based":
            print("andrew is literaly the best person ever")
        elif self.type == "briger":
            print("i am stupid and smelelly and bad and unfuny and ugly and i cri all day becasue ima weak baby man")
        else:
            print("you are based :)")
    
    def __giveage(this):
        print("I am " + str(this.age) + " years old")

    def __givemaerial(it):
        print("I am made of " + it.maerial)
    
    def declarebeing(self):
        self.__givemaerial()
        self.__giveage()

    #getters

    def getName(self):
        return self.__name
    
    #setters

    def setName(self, name):
        if self.__name != "Shane":
            self.__name = name

class coollist:
    item = None

    def additem(self):
        