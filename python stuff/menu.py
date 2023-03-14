#this library is imported for one job
import os
#seting up some of my variables, the rest are set up in the loop
total = 0
servis = True
nochicken_comb = "no"
#this is the only reason i have it 
os.system("cls")

print("Hi and welcom to big burg the home of the big burg")

#start of the loop :)
while servis:
    #yay the library
    os.system("cls")

    #this one if statement contains everything *pain*
    big_burg = input("can i intrest you in our big burg for 15.50$? ")
    #got to have them options
    if big_burg == "yes" or big_burg == "Yes" or big_burg == "ja" or big_burg == "si" or big_burg == "da"  or big_burg == "y" or big_burg == "Y":
        big_burg_comb = input("would you like to make it a combo for 20.00$ ")

        if big_burg_comb == "yes" or big_burg_comb == "Yes" or big_burg_comb == "ja" or big_burg_comb == "si" or big_burg_comb == "da":
            total += 20
            #the soda goes no where it is to decive the user
            soda = input("what flavor of soda would you like? ")

            #this anything else is the only way to break the loop and get your total
            anything_else = input("My pleasher, is their anything else I can help you with today? ")
            if anything_else == "yes" or anything_else == "Yes" or anything_else == "ja" or anything_else == "si" or anything_else == "da":
                servis = True
            elif anything_else != "yes" or anything_else != "Yes" or anything_else == "ja" or anything_else != "si" or anything_else != "da": 
                servis = False

        elif big_burg_comb == "no" or big_burg_comb == "No" or big_burg_comb == "nine" or big_burg_comb == "NO" or big_burg_comb == "neyt":
            total += 15.50
            anything_else = input("My pleasher, is their anything else I can help you with today?")
            if anything_else == "yes" or anything_else == "Yes" or anything_else == "ja" or anything_else == "si" or anything_else == "da":
                servis = True
            elif anything_else != "yes" or anything_else != "Yes" or anything_else == "ja" or anything_else != "si" or anything_else != "da": 
                servis = False

    elif big_burg == "No" or big_burg == "no" or big_burg == "nine" or big_burg == "neyt":
        menu = input("would you like to see the menu? ")
        if menu == "yes" or menu == "Yes" or menu == "ja" or menu == "si" or menu == "da":
            #this is as prity as im going to make it
            print("Alrighty, here is the menu")

            print("***************")
            print("MENU")
        

            print("***************")
            print("Main orders")
            print("***************")

            print("--------------")
            print("big burg")
            print("cost: 15.50$")
        

            print("--------------")
            print("chicken sandwich")
            print("cost: 11.00$")
        

            print("--------------")
            print("smol burg")
            print("cost: 9.50$")
        

            print("***************")
            print("fries")
            print("***************")
        
            print("--------------")
            print("large")
            print("cost: 6.00$")
        

            print("--------------")
            print("mid")
            print("cost: 5.00$")
        

            print("--------------")
            print("smol")
            print("cost: 4.00$")

            print("--------------")
            print("soda")
            print("cost: 4.50$")

            print("--------------")
            print("water")
            print("cost: 0.00$")


        else:
            #you cant not order if you try to not it just starts over, you must pucase product
            order = input("what would you like? ")
            if order == "big burg":
                #this is a great time to mention that i dont know how much things sould cost, i just gused, everything might be super overpriced but i dont care sue me
                big_burg_comb = input("would you like to make it a combo for 20.00$ ")

                if big_burg_comb == "yes" or big_burg_comb == "Yes" or big_burg_comb == "ja" or big_burg_comb == "si" or big_burg_comb == "da":
                    total += 20
                    soda = input("what flavor of soda would you like? ")
                    anything_else = input("My pleasher, is their anything else I can help you with today? ")
                    if anything_else == "yes" or anything_else == "Yes" or anything_else == "ja" or anything_else == "si" or anything_else == "da":
                        servis = True
                    elif anything_else != "yes" or anything_else != "Yes" or anything_else == "ja" or anything_else != "si" or anything_else != "da": 
                        servis = False
                        
                elif big_burg_comb == "no" or big_burg_comb == "No" or big_burg_comb == "nine" or big_burg_comb == "NO" or big_burg_comb == "neyt":
                    total += 15.50
                    anything_else = input("My pleasher, is their anything else I can help you with today? ")
                    if anything_else == "yes" or anything_else == "Yes" or anything_else == "ja" or anything_else == "si" or anything_else == "da":
                        servis = True
                    elif anything_else != "yes" or anything_else != "Yes" or anything_else == "ja" or anything_else != "si" or anything_else != "da": 
                        servis = False

            elif order == "chicken sandwich":
                        #mmm chicken sandwich
                        chicken_comb = input("would you like to make it a combo for 15.00$ ")

                        if chicken_comb == "yes" or chicken_comb == "Yes" or chicken_comb == "ja" or chicken_comb == "si" or chicken_comb == "da":
                            total += 15
                            soda = input("what flavor of soda would you like? ")
                            anything_else = input("My pleasher, is their anything else I can help you with today? ")
                            if anything_else == "yes" or anything_else == "Yes" or anything_else == "ja" or anything_else == "si" or anything_else == "da":
                             servis = True
                            elif anything_else != "yes" or anything_else != "Yes" or anything_else == "ja" or anything_else != "si" or anything_else != "da": 
                              servis = False
                                
                        elif chicken_comb == "no" or chicken_comb == "No" or chicken_comb == "nine" or chicken_comb == "NO" or chicken_comb == "neyt":
                            total += 11.0
                            anything_else = input("My pleasher, is their anything else I can help you with today? ")
                            if anything_else == "yes" or anything_else == "Yes" or anything_else == "ja" or anything_else == "si" or anything_else == "da":
                             servis = True
                            elif anything_else != "yes" or anything_else != "Yes" or anything_else == "ja" or anything_else != "si" or anything_else != "da": 
                              servis = False
            
            elif order == "smol burg":
                        #lol
                        print("you dont get combos")
        
                        total += 11.0
                        anything_else = input("Is their anything else I can help you with today? ")
                        if anything_else == "yes" or anything_else == "Yes" or anything_else == "ja" or anything_else == "si" or anything_else == "da":
                            servis = True
                        elif anything_else != "yes" or anything_else != "Yes" or anything_else == "ja" or anything_else != "si" or anything_else != "da": 
                             servis = False
            
            elif order == "large fries" or order ==  "fry large" or order ==  "a large fry":
                        
                        #i should have mentioned that you get fryes in the combos
                        total += 6.0
                        anything_else = input("Is their anything else I can help you with today? ")
                        if anything_else == "yes" or anything_else == "Yes" or anything_else == "ja" or anything_else == "si" or anything_else == "da":
                            servis = True
                        elif anything_else != "yes" or anything_else != "Yes" or anything_else == "ja" or anything_else != "si" or anything_else != "da": 
                            servis = False
            
            elif order == "mid fries" or order == "fry mid" or order == "a mid fry":
                        
                        #actualy you can cry about it
                        total += 5.0
                        anything_else = input("Is their anything else I can help you with today? ")
                        if anything_else == "yes" or anything_else == "Yes" or anything_else == "ja" or anything_else == "si" or anything_else == "da":
                            servis = True
                        elif anything_else != "yes" or anything_else != "Yes" or anything_else == "ja" or anything_else != "si" or anything_else != "da": 
                            servis = False

            if order == "smol fries" or order == "fry smol" or order == "a smol fry":
                        
                        #you might get frys in your combo and if you dont you wont know, (your not actualy geting food)
                        total += 4.0
                        anything_else = input("Is their anything else I can help you with today? ")
                        if anything_else == "yes" or anything_else == "Yes" or anything_else == "ja" or anything_else == "si" or anything_else == "da":
                            servis = True
                        elif anything_else != "yes" or anything_else != "Yes" or anything_else == "ja" or anything_else != "si" or anything_else != "da": 
                            servis = False

            elif order == "soda":
                soda_size = input("what size would you like we have larg mid and smol? ")

                if soda_size == "larg":
                    total += 4.50
                    soda = input("what flavor would you like? ")
                
                    anything_else = input("Is their anything else I can help you with today? ")
                    if anything_else == "yes" or anything_else == "Yes" or anything_else == "ja" or anything_else == "si" or anything_else == "da":
                        servis = True
                    elif anything_else != "yes" or anything_else != "Yes" or anything_else == "ja" or anything_else != "si" or anything_else != "da": 
                        servis = False
                
                elif soda_size == "mid":
                    total += 3.50
                    soda = input("what flavor would you like? ")
                
                    anything_else = input("Is their anything else I can help you with today? ")
                    if anything_else == "yes" or anything_else == "Yes" or anything_else == "ja" or anything_else == "si" or anything_else == "da":
                        servis = True
                    elif anything_else != "yes" or anything_else != "Yes" or anything_else == "ja" or anything_else != "si" or anything_else != "da": 
                        servis = False

                elif soda_size == "smol":
                    total += 2.50
                    soda = input("what flavor would you like? ")
                
                    anything_else = input("Is their anything else I can help you with today? ")
                    if anything_else == "yes" or anything_else == "Yes" or anything_else == "ja" or anything_else == "si" or anything_else == "da":
                        servis = True
                    elif anything_else != "yes" or anything_else != "Yes" or anything_else == "ja" or anything_else != "si" or anything_else != "da": 
                        servis = False
                
                else:
                    #here you can see when i gained an extra brain cell remembering that i sould have a way to help peopel if they input incorectly.
                    print("we dont have that size ")
                    anything_else = input("Is their anything else I can help you with today? ")
                    if anything_else == "yes" or anything_else == "Yes" or anything_else == "ja" or anything_else == "si" or anything_else == "da":
                        servis = True
                    elif anything_else != "yes" or anything_else != "Yes" or anything_else == "ja" or anything_else != "si" or anything_else != "da":
                        servis = False
    #this line of code serves no purpous but if i get rid of it everything breaks, and no im not going to fix it
    if not servis:
        input("cringe or press enter")


                
#this is the math for the total look i even put a dollor sign
print("great your total is " + str(total) + "$")


