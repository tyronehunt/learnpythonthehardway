# Note there are similarities between modules and dictionaries
# mystuff['apple'] will get an apple from dict
# mystuff.apple() will get apple function from an imported module
# mystuff.apple will get a variable name apple from an imported module

# Class are like modules - they group functions and data and place them inside a container so you can access them with . operator
""" The reason classes are used instead of modules is because with a class you can use it to craft millions at a time,
 each one doesn't interfere with the next. With a module you can only import one for the entire programme """

 # Objects are like import (like when you import a module, but you instantiate a class to get an object)
 # You call a Class in the same way you would call a function, i.e. variable =  ClassName(arguments)

""" I now have three ways to get things from things
- dict style
 mystuff['apples']

 - module style
 mystuff.apples() for a function
 mystuff.tangerine for a variable

 - class style
 thing = MyStuff() to create the object
 thing.apples() for a function
 thing.tangerine for a variable
"""

class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics
    
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_bday = Song(["Happy birthday to you",
"I don't want to get sued",
"So I'll stop right there!"
])

bulls_on_parade = Song(["They rally around tha family","with pockets full of shells"])

bryan_adams=Song(["Look into my eyes","You will see","what you mean to me"])

the_calling = Song(["so lately","been wondering","who will be there to take my place"])

test_variable = ["this is a test variable","not a great song lyric"]
test_song = Song(test_variable)

happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()
bryan_adams.sing_me_a_song()
the_calling.sing_me_a_song()
test_song.sing_me_a_song()