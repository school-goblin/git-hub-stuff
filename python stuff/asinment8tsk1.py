import random
import turtle as tur
from pattern import *
curenthead = 0
def main():
    # Setup pattern
    setup()
    # Play again loop
    playAgain = True
    while playAgain:
        # Present a menu to the user
        # Let them select mode
        print("Choose a mode")
        print("1) Rectangle Pattern")
        print("2) Circle Pattern")
        print("3) Super Pattern")
        mode = eval(input("Which mode do you want to play? 1, 2 or 3: "))
        # If they choose 'Rectangle Patterns'
        if mode == 1:
            
        #### Add Input Statement(s) as needed ####
            centerX = intput("what is the centar x: ")
            centerY = intput("what is the centrear y: ")
            offset = intput("what is the offset: ")
            width = intput("what is the width: ")
            height = intput("what is the height: ")
            count = intput("how many times: ")
            rotation = intput("what is the ratation: ")

            andrewtate = 360 / count

            #### End Add Inputs Statement(s) ####
            # Draw the rectangle pattern
            drawRectanglePattern(centerX, centerY, offset, width, height,
            count, rotation, andrewtate, curenthead)
        # If they choose 'Circle Patterns'
        elif mode == 2:
        
            #### Add Input Statement(s) as needed ####
            centerX = intput("what is the centar x: ")
            centerY = intput("what is the centrear y: ")
            offset = intput("what is the offset: ")
            radius = intput("what is the radis: ")
            count = intput("how many times: ")

            andrewtate = 360 / count
            #### End Add Inputs Statement(s) ####
            # Draw the circle pattern
            drawCirclePattern(centerX, centerY, offset, radius, count, andrewtate, curenthead)
            # If they choose 'Super Patterns'
        
        elif mode == 3:
        #### Add Input Statement(s) as needed ####
            count = intput("how many shapes: ")
            andrewtate = 360 / count
        #### End Add Inputs Statement(s) ####
            if count > 0:
                drawSuperPattern(count, andrewtate)
            
                
       
            # Play again?
        while True:
            print("Do you want to play again?")
            print("1) Yes, and keep drawings")
            print("2) Yes, and clear drawings")
            print("3) No, I am all done")
            response = input("Choose 1, 2, or 3: ")
            #### Add Statement(s) to clear drawings and play again ####
            if response == "1":
                playAgain = True
                break
            elif response == "2":
                  playAgain = True
                  reset()
                  break
            elif response == "3":
                print("Thanks for playing!")
                done()
                playAgain = False
                break
            else:
                print("not a valid responce, please input 1, 2 or 3: ")
                
main()