""" Use a list whenever you have something that matches the list data structure's useful features
1. If you need to maintain order. This is a listed order, not a sorted order. Lists do not sort for you. 
2. If you need to access contents randomly by number. Remember cardinal number starting at 0
3. If you need to go through the contents linearly (first to last). That's what for loops are for. 
"""

ten_things = "Apples Oranges Crows Telephone Light Sugar"

print ("Wait there aint 10 things on that list, let's fix that")

stuff = ten_things.split(' ')
more_stuff = ['Day', 'Night', 'Song', 'Frisbee', 'Corn', 'Banana', 'Girl', 'Boy']

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("Adding:", next_one)
    stuff.append(next_one)
    print(f"There are {len(stuff)} items now.")

print ("There we go: ", stuff)

print ("Let's do some things with stuff")

print (stuff[1])
print (stuff[-1])
print (stuff.pop())
print (' '.join(stuff))
print ('#'.join(stuff[3:5]))