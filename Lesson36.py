from sys import exit
from time import sleep


def left_room():
    print "In this room, you find a midget with a stick."
    print "He says 'Take this stick, it will help you'."

    print "Do you take the stick? "

    response = raw_input(">")

    if "take" in response or "yes" in response:
        print "You take the stick from the midget. He farts and runs away."
        stick = True
        print "You feel as if there's nothing left to do in this room and return to the main room."
        sleep(2)
        main_room(stick)
    else:
        print "You decide to leave the stick. That midget looks like he needs to fart, better get out of here."
        stick = False
        print "You feel as if there's nothing left to do in this room and return to the main room."
        sleep(2)
        main_room(stick)


def right_room(stick):
    if not stick:
        print "You enter the room and a slightly less farty midget throws a rock at your head. "
        print "Without a stick to defend yourself, you get hit right between the eyes.\n"
        dead("You fall to the floor and die.")
    else:
        print "You enter the room and a farty midget throws a rock at your head."
        print "With a stick to defend yourself, you easily swat the rock away."
        print "It hits the midget who lets out an Earth shattering fart and then runs away."
        print "That was a close one!\n"
        dead("In this room you find the treasure. You have won!")


def dead(reason):
    print reason
    restart = raw_input("Would you like to restart?: Type yes or no >")
    if "yes" in restart:
        start()
    else:
        exit()


def main_room(stick):
    print "You have entered the main room of the house. There is a smell of old cheese in the air."
    print "You realize that the smell is coming from your feet. You are a smelly adventurer."
    print "You see a hallway ahead, there are two doors there. One on the left and one on the right. What do you do?\n"

    action = raw_input(">")
    if "left" in action:
        stick = left_room()
    elif "right" in action:
        right_room(stick)
    else:
        dead("Confused and smelling of cheese, you wander around till you die.")


def start():
    print "You find yourself at the door of an old house. There has been rumors that there is treasure inside."
    print "There has also been rumors that no one has ever made it out of the house alive! You're not one for rumors, "
    print "and you have some time to kill... so you decide to go inside."
    print "\nAre you ready to enter the house?\n"

    response = raw_input("Type yes or no >")

    print "\nWho cares, you're going in anyway!\n"

    print "You slowly count to 10 to ease your nerves.\n"
    for i in range(0, 10):
        print i
        sleep(1)
    print "\n'TEN!' you yell out as you run through the door to the house!\n"

    stick = False

    main_room(stick)


start()
