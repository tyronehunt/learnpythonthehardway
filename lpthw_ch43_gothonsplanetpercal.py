from sys import exit
from random import randint
from textwrap import dedent

# the dedent function from textwrap module helps us write room descriptions with triple quotes """ and strips the white-space from the beginning if lines.

class Scene(object):

    def enter(self):
        print("This scene is not yet configured.")
        print("subclass it and implement enter().")
        exit(1)

# This is a base class with properties for all scenes, in this example the base doesn't do much

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        # This code calls the opening_scene function from the Map class on the instance of Map passed to Engine and sets it equal to the current_scene
        current_scene = self.scene_map.opening_scene()
        # This code tells the programme what the last_scene is called, note it's an object, not a string
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

            # print out the last scene
            current_scene.enter()

class Death(Scene):

    quips = ["You died. You kinda suck at this",
            "You Mom would be proud... if she were smarter",
            "Such a loser",
            "I have a small puppy that's better at this",
            "You're worse than your Dad's jokes"
            ]

    def enter(self):
        print(Death.quips[randint(0, len(self.quips)-1)])
        exit(1)

class CentralCorridor(Scene):

    def enter(self):
        print(dedent("""
            The Gothons of Planet Percal #25 have invaded your ship and destroyed your entire crew. You are the last surviving
            member and your last mission is to get the neutron destruct bomb from the Weapons Armory, put it in the bridge
            , and blow the ship up after getting into an escape pod. 

            You're running down the central corridor to the Weapons Armory when a Gothon jumps out, red scaly skin, dark grimy
            teeth, and evil clown costume flowing around his hate filled body. He's blocking the door to the Armory and about to pull a weapon
            to blast you
            """))

        action = input("> ")

        if action == "shoot!":
            print(dedent("""
                Quick on the draw you yank our your blaster and fire it at the Gothon. His clown costume is flowing and moving around his body, 
                which throws off your aim. Your laser hits his costume, but misses him entirely. This completely ruins his brand new constume his mother bought him, 
                which makes him fly into an insance rage and blast you repeatedly in the face until you are dead. 
                """))
            return 'death'

        elif action == "dodge!":
            print(dedent("""
                Like a world class boxer you dodge, weave, slip and slide right as the Gothon's blaster cranks a laser past your head. In the middle of your
                artful dodge your foot slips and you bang your head on the metal wall and pass out. You wake up shortly after only to die as the
                Gothon stomps on your head. 
                """))
            return 'death'

        elif action =="tell a joke":
            print(dedent("""
                Lucky for you they made you learn Gothon insults in the academy. you tell the one Gothon joke you know: 
                sdf asdf fagonona aepupasdf fa;asdlians. The Gothon stops, tries not to laugh, then bursts out laughing and can't move. 
                While he's still laughing you run up and shoot him square in the head putting him down, then jump through the weapon armoury door.
                """))
            return 'laser_weapon_armory'

        else:
            print("Enter a valid choice")
            return 'central_corridor'

class LaserWeaponArmery(Scene):

    def enter(self):
        print (dedent("""
            You do a dive roll into the Weapon Armory, crouch and scan the room for more Gothons that might be hiding. It's dead quiet, too quiet. 
            You stand up and run to the far side of the room and find the neutron bomb in its container. There's a keypad lock on the box and you need the code to get
            the bomb out. If you get the code wrong 10 times then the lock closes forever and you can't get the bomb. The code is 3 digits. 
            """))
    
        code = f"{randint(1,9)}{randint(1,9)}{randint(1,9)}"
        guess = input("[keypad]> ")
        guesses = 0

        while guess != code and guesses < 10:
            print("BZZZZZDDD")
            guesses += 1
            guess = input("[keypad]> ")

        if guess == code:
            print(dedent("""
                The container clicks open and the seal breaks, letting gas out. You grab the neutron bomb and 
                run as fast as you can to the bridge where you must place it in the right spot.
                """))
            return 'the_bridge'
    
        else:
            print(dedent("""
                The lock buzzes one last time and then you hear a sickening melting sound as the mechanism is fused together. You decide to sit there, and finally the
                Gothon blo up your ship and you die. 
                """))
            return 'death'

class TheBridge(Scene):
    
    def enter(self):
        print(dedent("""
            You burst onto the Bridge with the neutron destruct bomb under your arm and surprise 5 Gothons who are trying to take control of the ship. 
            Each of them has an even uglier clown costume than the last. They haven't pulled their weapons out yet, as they see the active bomb under your arm and don't want to set it off. 
            """))

        action = input('> ')

        if action == "throw the bomb":
            print(dedent("""
                In a panic you throw the bomb at the group of Gothons and make a leap for the door. Right as you drop it a Gothon shoots you in the back, killing you. 
                You die knowing they'll probably blow up as you die
                """))
            return 'death'
    
        elif action == "slowly place the bomb":
            print(dedent("""
                You point your blaster at the bomb under your arm and the Gothons put their hands up and start to sweat. You inch backwards to the door, open it and then carefully place the bomb on the floor. 
                You then jump back from the door, punch the close button and blast the lock. You make an escape. 
                """))
            return 'escape_pod'
    
        else:
            print ("does not compute!")
            return 'the_bridge'

class EscapePod(Scene):

    def enter(self):
        print(dedent("""
        You rush through the ship desperately trying to make it to the escape pod before the ship explodes. You get to the chamber with escape pods and need to pick one to take. 
        Some pods are damaged, which pod do you take?
        """))

        good_pod = randint(1,5)
        guess = input("[pod #]> ")

        if int(guess) != good_pod:
            print(dedent("""
        You jump into pod {guess} and hit the eject button. The pod escapes into space and then implodes, crushing you. 
        """))
            return Death
        
        else:
            print(dedent("""
        Miraculously the pod works, you escape and win this silly game!
        """))
            return 'finished'

class Finished(Scene):
    def enter(self):
        print ("You won! Good job!")
        return 'finished'

class Map(object):

    # You can see that each scene Class is stored in a dictionary called scenes and named with a string.
    # The dictionary is referred to with Map.scenes. This is also why Map comes after scenes, because they have to exist for the dictionary to know them
    
    scenes = {
        'central_corridor': CentralCorridor(),
        'laser_weapon_armory': LaserWeaponArmery(),
        'the_bridge': TheBridge(),
        'escape_pod': EscapePod(),
        'death': Death(),
        'finished': Finished(),
    }
    
    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)


# Finally this code maps a Map, then hands that to an Engine before calling play to make the game work. 
a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()

""" How this game works: 
1. make an instance of the Map class called a_map. This has an attribute called a start_scene such that typing a_map.start_scene returns 'central_corridor'
2. make an instance of the Engine class. The object 'a_map' is stored in the variable a_game.scene_map
3. call the play function from the Engine class on the a_game instance of Engine
4. set the current_scene equal to the opening_scene function
5. this opening_scene function instantly calls the next_scene function (both within the Map class)
6. the next_scene function returns the value associated with the key in the scenes dictionary (also in Map class)
7. then back inside the engine, a while loop runs until the current class being run is equal to the final class specified
8. until that point, the while loop will launch the enter() function on the current_scene object
9. each class is a sub-class of the Scene object and runs a piece of code, setting the return value equal to a string - a name of the next scene
10. the engine will then redirect to the Map Class to match this string to a Class object
11. the engine will re-route to the next Class function and so on...

"""