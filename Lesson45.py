from random import randint
from time import sleep
import os


def death(reason):

    print reason
    ending = randint(1, 4)

    if ending == 1:
        print "You have failed as an adventurer. You're last thoughts as you lay dying are\n" \
              "about how lame you are."
    elif ending == 2:
        print "Well that's one way to end your adventure. Maybe in a few hundered years\n" \
              "someone will find your body!"
    elif ending == 3:
        print "You are really not good at this! Maybe you should try something easier, like\n" \
              "planting flowers or eating pickles!"
    else:
        print "As you slowly blackout, you realize that you forgot to feed your cats before\n" \
              "you left on  your adventure. WHO'S GOING TO TAKE CARE OF THEM NOW?!?!"
        restart()


def restart():

    respawn = raw_input("Would you like to play again?> ")

    if "yes" in respawn:
        start()
    else:
        print "Fine, it's probably best if you give up!"
        exit()


def start(inventory):

    print "You are the worlds greatest treasure hunter! Well, that's what you tell \n" \
          "people anyway. On a recent trip to Kirkland's, you discovered an old map hidden\n" \
          "behind a large pot of stinky potpourri. You quickly pay for the map and start\n" \
          "to prepare for your greatest adventure yet! This could be it! This could be your\n" \
          "ticket to fame and fortune!\n\n"

    sleep(1)

    print "According to the map, you must start your journey at the entrance to DEATH MOUNTAIN!\n" \
          "Death mountain does sound pretty scary. You decide that it should be renamed SPARKLE\n" \
          "PRINCESS MOUNTAIN!! That's much better. You find the entrance and go inside.\n\n"

    raw_input(">")
    os.system('cls')

    cave_entrance(inventory)

def dark_room(inventory):

    print "Dark room"

    action = raw_input("> ")

    if inventory.get("light") == True:

        print "ligth!"

    else:

        print "oh's no's!!"

        death("You can't see in the dark dummy!")

    if "stuff" in action:

        print "Yeah!"

        cave_entrance(inventory)

    else:

        print "da poops!"

        death("You done gone and got the poops!")

    cave_entrance(inventory)

def cave_entrance(inventory):

    print "The main cavern of DEATH MOU... I mean, SPARKLE PRINCESS MOUNTAIN is very large.\n" \
          "You can hear the faint noise of water flowing from deep within the cave. It it rather \n" \
          "cold in the cave and it smells very wet and moldy.\n\n"

    sleep(1)

    print "On your left you see a winding path that leads to a dark tunnel. On your right, there is a\n" \
          "nice little tourist info station! Straight ahead is another tunnel leading deep into the cave.\n\n"

    sleep(1)

    print "What would you like to do?"

    action = raw_input('>: ')

    if "left" in action:

        print "things"

        dark_room(inventory)

    elif "right" in action:

        print "things"

        kiosk(inventory)

    elif "straight" in action or "forward" in action:

        print "things"

        deep_tunnel(inventory)

    else:

        print "things"

        cave_entrance(inventory)

def kiosk(inventory):

    print "things"

    action = raw_input("> ")

    if "open" in action and "box" in action:

        print "things"

         = True

    else:

        print "things"

        kiosk(inventory)


inventory = {"name":"Bob", "rope":False, "light":True}
os.system('cls')
start(inventory)
