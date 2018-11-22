import random
import time

def intro():
    print()
    print("It is the zombie apocolypse.")
    print("You must survive at all costs.")
    print("Choices you make will directly affect you and those around you.")
    print("In the new reality, you either thrive or you die.")
    print()
    ready = ""
    while ready != "1":
        ready = input("Are you ready? Enter 1 to continue. ")
    print()
    print("First game choice")
    print()

def choosePath():
    path = ""
    while path != "1" and path != "2":
        path = input("Which path will you choose? (1 or 2): ")
    return path

def checkPath(chosenPath):
    print()
    print("Something happened")
    time.sleep(2)
    print()
    print("something else")
    time.sleep(2)
    print()
    correctPath = random.randint(1, 2)
    if chosenPath == str(correctPath):
        print("something good happens")
        print()
    else:
        print("Something bad happens")
        print()
        # Run the losing game function

playAgain = "yes"
while playAgain == "yes" or playAgain == "y":
    intro()
    choice = choosePath()
    checkPath(choice)
    playAgain = input("Do you want to play again? (yes or y to continue): ")
