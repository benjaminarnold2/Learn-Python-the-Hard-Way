from sys import exit
from random import randint


class Scene(object):

    def enter(self):
        print "This scene is not yet configured. Subclass it and implement enter()"
        exit(1)


class Engine(object):
    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()

        while True:
            print "\n-------------"
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)


class Death(Scene):
    quips = [
        "You died. Nobody is surprised",
        "Well, that wasn't the right move, was it.",
        "Sad trombone!!",
        "Momo would have done better!!"
    ]

    def enter(self):
        print Death.quips[randint(0, len(self.quips)-1)]
        exit(1)


class CentralCorridor(Scene):
    def enter(self):
        print "story"

        action = raw_input("> ")

        if 'shoot' in action:

            print "story"

            return 'death'
        elif 'dodge' in action:

            print "story"

            return 'death'

        elif 'joke' in action:

            print 'Ha!'

            return 'laser_weapon_armory'

        else:
            print "You've successfully confused yourself."

            return 'central_corridor'


class LaserWeaponArmory(Scene):

    def enter(self):

        print "story"

        code = "%d%d%d" % (randint(1, 9), randint(1, 9), randint(1, 9),)
        guess = raw_input("[keypad]> ")
        guesses = 0

        while guess != code and guesses < 9:

            print "BZZZZZZDD!!!"
            if guesses > 7:
                print code
            guesses += 1
            guess = raw_input("[keypad]> ")
        if guess == code:
            print "code guessed"
            return "the_bridge"
        else:
            print "bad things man"
            return 'death'


class TheBridge(Scene):

    def enter(self):

        print 'things'

        action = raw_input('> ')

        if 'throw' in action and 'bomb' in action:

            print 'action!'
            return 'death'

        elif 'slowly' in action or 'place' in action:

            print 'easy does it'
            return 'escape_pod'

        else:

            print "picking your nose doesn't help anyone"
            return 'the_bridge'


class EscapePod(Scene):

    def enter(self):

        print 'things'

        good_pod = randint(1, 5)
        guess = raw_input("[pod #]> ")

        if int(guess) != good_pod:
            print "bam!"
            return 'death'

        else:

            print 'end!'
            return 'finished'


class Map(object):

    scenes = {
        'central_corridor': CentralCorridor(),
        'laser_weapon_armory': LaserWeaponArmory(),
        'the_bridge': TheBridge(),
        'escape_pod': EscapePod(),
        'death': Death()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        return Map.scenes.get(scene_name)

    def opening_scene(self):
        return self.next_scene(self.start_scene)


a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
