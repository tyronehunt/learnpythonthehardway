""" The process to build something with Python and object-orientated programming - top down
1. Write or draw about the problems
2. Extract key concepts from 1 and research them
3. Create a class hierarchy and object map for the concepts
4. Code the classes and a test to run them
5. Repeat and refine

Loosely speaking if you write in english, the nouns will end up providing a class hierarchy and the verbs the functions

For example the sentence 'Aliens have invaded a shape ship and our hero has to go through the maze of rooms defeating
them so he can escape into an escape pod to the planet below. The game will be more like Zork or adventure type game with
text outpurs and funny ways to die. The game will involve an engine that runs a map full of rooms or scenes. Each room
will print its own description when the player enters it and then tell the engine what room to run next out of the map'

The list of nouns: alien, player, ship, maze, room, scene, gothon, escape pod, planet, map, engine, death, corridor, laser weapon armory, the bridge

This turns into a class hierarchy:
* Map
* Engine
* Scene
    - death
    - corridor
    - laser weapon armery 
    - the bridge
    - escape pod

Which can then have actions attached:
* Map
- next_scene
- opening_scene
* Engine
- play
*Scene
- enter
    - death
    - corridor
    - laser weapon armery
    - the bridge
    - escape pod
"""

class Scene(object):

    def enter(self):
        pass

class Engine(object):

    def __init__(self, scene_map):
        pass

    def play(self):
        pass

class Death(Scene):

    def enter(self):
        pass

class CentralCorridor(Scene):

    def enter(self):
        pass

class LaserWeaponArmery(Scene):

    def enter(self):
        pass

class TheBridge(Scene):
    def enter(self):
        pass

class EscapePod(Scene):

    def enter(self):
        pass

class Map(object):

    def __init__(self, start_scene):
        pass

    def next_scene(self, scene_name):
        pass

    def opening_scene(self):
        pass

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()

""" The bottom-up process to build code is:
1. take a small piece of the problem, hack it and get it to barely work
2. refine the code into something more formal with classes and automated tests
3. extract the key concepts you're using and research them
4. write a description of whats really going on
5. go back and refine the code, possibly throwing it out and starting over
6. repeat, moving on to some other piece of the problem """