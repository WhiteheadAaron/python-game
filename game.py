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
    print("You are at your family house with your parents, teenage brother, and younger sister.")
    time.sleep(2)
    print()
    print("Your dad wants to go to the store to get supplies. Your mom thinks you should stay put.")
    time.sleep(2)
    print()
    print("Choice 1 is going to the store, choice 2 is waiting at home and barricading the doors")
    print()


def choosePath():
    path = ""
    while path != "1" and path != "2":
        path = input("Which path will you choose? (1 or 2): ")
    return path


path1 = ""


def chooseDirection(chosenPath):
    if chosenPath == "1":
        return storePath()
    else:
        return stayHomePath()


def stayHomePath():
    print()
    print("You decide to stay at home, and prepare for the worst.")
    time.sleep(2)
    print()
    print("Your dad and brother go to the garage to get supplies to board up the house.")
    time.sleep(2)
    print()
    print("In the meantime, you hear screaming outside in the street. It sounds like your neighbor.")
    time.sleep(2)
    print()
    print("Your mom urges you to stay inside, but you want to save your childhood friend.")
    time.sleep(2)
    print()
    response = ""
    while response != "1" and response != "2":
        response = input(
            "Enter 1 to stay inside, 2 to go help your friend: ")
    checkHomePath(response)


def checkHomePath(chosenPath):
    friendChoice = ""
    print()
    if chosenPath == "1":
        print("The screams continue for several minutes, but they eventually fade away.")
        time.sleep(2)
        print()
        print("You look out the window to try to get a view of what happened, but you can't see anything.")
        makeChoice()
    if chosenPath == "2":
        print("Despite your mother's pleas, you sprint outside to try to save your friend.")
        time.sleep(2)
        print()
        print("You see him on his back, keeping the zombie off by holding a bat to it's neck horizontally.")
        time.sleep(2)
        print()
        print("You see a large stick on the ground. Do you run across to get the stick first, or go straight to help?")
        time.sleep(2)
        print()
        while friendChoice != "1" and friendChoice != "2":
            friendChoice = input(
                "Enter 1 to get the stick, enter 2 to help immediately: ")

        correctChoice = random.randint(1, 2)
        if friendChoice == str(correctChoice):
            if friendChoice == "1":
                print(
                    "You grab the stick, and get to your friend just in time to save him.")
                time.sleep(2)
                print()
                print(
                    "He thanks you profusely, and returns home to see his family again.")
                makeChoice()
            else:
                print(
                    "You run to your friend, and kick the zombie off of him. He runs back into his house, and you do the same.")
                time.sleep(2)
                print()
                print(
                    "He didn't have time to thank you, but I'm sure he is very grateful.")
                makeChoice()
        if friendChoice != str(correctChoice):
            print()
            print("Unexpectedly, a swarm of zombies comes from your blind spot. Your mother screams as she watches on.")
            time.sleep(2)
            print()
            print(
                "As you're being taken down, you see your friend engulfed by a swarm as well. The End.")
            playAgain()

            # Run the losing game function


def storePath():
    print()
    print("You leave the house, and set out for the store")
    time.sleep(2)
    print()
    print("You get to the store, and the parking lot looks empty")
    time.sleep(2)
    print()
    print("The front door is broken down, and you hear a noise inside of the store")
    time.sleep(2)
    print()
    response = ""
    while response != "1" and response != "2":
        response = input(
            "Enter 1 to go to the left side, 2 to go to the right side: ")
    checkStorePath(response)


def checkStorePath(chosenPath):
    correctPath = random.randint(1, 2)
    print()
    if correctPath == 1:
        print(
            "Suddenly on the right side of the store, you hear and see a horde of zombies")
        time.sleep(2)
        print()
        print("You scream, and you now have the full attention of the zombies.")
    if correctPath == 2:
        print("Suddenly on the left side of the store, you hear and see a horde of zombies")
        time.sleep(2)
        print()
        print("You scream, and you now have the full attention of the zombies.")
    time.sleep(2)
    print()
    if chosenPath == str(correctPath):
        print("Luckily for you, you chose the right side of the store.")
        time.sleep(2)
        print()
        print("You and your Dad are able to escape, gathering a small amount of food and medicine")
        makeChoice()
    else:
        print(
            "Unfortunately you chose the wrong side, and are quickly engulfed in the swarm")
        print()
        playAgain()


def homePath2():
    print()
    print("Your mom has had a change of heart, and she thinks it's time to leave the house.")
    time.sleep(2)
    print()
    print("The rest of the family agrees, it's too dangerous to stay here.")
    time.sleep(2)
    print()
    print("Your dad suggests you make the journey to his parents house. It's in a secluded area, and probably safer.")
    time.sleep(2)
    print()
    print("Mom wants to travel to the CDC. It's a bit further, but they could have a cure.")
    time.sleep(2)
    print()
    homeChoice = ""
    while homeChoice != "1" and homeChoice != "2":
        homeChoice = input(
            "Enter 1 to go to your grandparent's house, enter 2 to go to the CDC: ")
    print()
    return homeChoice


def makeChoice():
    number = homePath2()
    if number == "1":
        gmaPath()
    else:
        cdcPath()


def cdcPath():
    print("You set off to begin your journey to the CDC.")
    time.sleep(2)
    print()
    print("Do you want to drive on the interstate or the backroads?")
    time.sleep(2)
    print()
    print("The interstate will make the journey much quicker, if the road is clear. The side roads are slower, but probably safer.")
    time.sleep(2)
    print()
    cdcChoice = ""
    while cdcChoice != "1" and cdcChoice != "2":
        cdcChoice = input(
            "Enter 1 to take the interstate, enter 2 to take the side roads: ")
    if cdcChoice == "1":
        interstateChoice()
    else:
        sideRoadsChoice()


def interstateChoice():
    print("interstate")


def sideRoadsChoice():
    print("side roads")


def gmaPath():
    print("You set off to begin your journey to Grandma and Grandpa's house.")
    time.sleep(2)
    print()
    print("Do you want to drive on the interstate or the backroads?")
    time.sleep(2)
    print()
    print("The interstate will make the journey much quicker, if the road is clear. The side roads are slower, but probably safer.")
    time.sleep(2)
    print()
    gmaChoice = ""
    while gmaChoice != "1" and gmaChoice != "2":
        gmaChoice = input("Enter 1 to take the interstate, enter 2 to take the side roads: ")
    if gmaChoice == "1":
        interstateChoice()
    else:
        sideRoadsChoice()


def playAgain():
    intro()
    choice = choosePath()
    chooseDirection(choice)


playAgain()
