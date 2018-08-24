# ordinal number system == ordered, 1st;  cardinal == cars at random, 0
# animals = ['bear', 'tiger', 'penguin', 'zebra']
# bear = animals[0]

""" IMPORT RULES FOR IF-STATEMENT CODING
1. Every if statement must have an else
2. Never nest if statements more than 2 deep, always try do 1 deep
3. Treat if-statements like paragraphs, where each if-elif-else grouping is like a set of sentences. Put blank lines before and after
4. Boolean tests should be simple. If they're complex, move calculations to variables earlier in the function, use good names
"""

""" SUGGESTED WAY TO CODE
1. Write a list of tasks (i.e. kanban board in software language)
2. Pick the easiest thing
3. Write english version of code first
4. Write code, run, fix (do in small chunks)
"""


# Import the module 'exit from the sys package, which allows you to exit scripts, either without error (0) or with erros (1....200)
from sys import exit

# This is a function - which describes actions inside a room. Note that functions are not declared in order. 
def gold_room():
    print("This room is full of gold. How much do you take?")

    choice = input("> ")
    if "0" in choice or "1" in choice:
        how_much = int(choice)
    else:
        dead("Man, learn to type a number.")

    if how_much < 50:
        print("Nice, you're not greedy, you win!")
        exit(0)
    else:
        dead("You greedy bastard!")

def bear_room():
    print("""
    There is a bear here. 
    The bear has a bunch of honey.
    The fat bear is in front of another door.
    How are you going to move the bear?""")
    bear_moved = False

    while True:
        choice = input("> ")

        if choice == "take honey":
            dead("The bear looks at you and then slaps your face off.")
        elif choice == "taunt bear" and not bear_moved:
            print("Thea bear has moved from the door \nYou can go through it now.")
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print("I got not idea what that means.")

def cthulhu_room():
    print("""
    Here you see the great evil Cthulhu.
    He, it, whatever stares at you and you go insance.
    Do you flee for your life or eat your head?""")
    choice = input("> ")

    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Well that was nasty!")
    else: 
        cthulhu_room()

def dead(why):
    print(why, "Good job!")
    exit(0)


def start():
    print("""
    You are in a dark room. 
    There is a door to your right and left.
    Which one do you take?""")

    choice = input("> ")

    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")

start()