# Inheritance is hard - avoid if possible. Most of the uses of inheritance can be replaced with composition, amd multiple inheritance should be avoided at all costs. 
# in the example class Foo(Bar) - this works as you can put common functionality of the Bar class into the more detailed Foo class
# Actions on the child imply an action on the parent, or over-ride the parent, or alter the action of the parent

# IMPLICIT INHERITANCE - define a function in the parent but not in the child
class Parent(object):

    def implicit(self):
        print("PARENT implicit()")

class Child(Parent):
    pass

dad = Parent()
son = Child()

dad.implicit()
son.implicit()

# OVERRIDE EXPLICITLY - if you call functions implicitly you can't have the child behave differently

class Parent2(object):

    def override(self):
        print("PRINT override()")

class Child2(Parent2):

    def override(self):
        print("CHILD override()")

dad = Parent2()
son = Child2()

dad.override()
son.override()

# ALTERED - first override parent function with child, then use super to get Parent version to call.

class Parent3():

    def altered(self):
        print("PARENT altered()")

class Child3(Parent3):

    def altered(self):
        print("CHILD, BEFORE PARENT altered()")
        super(Child3, self).altered()
        print("CHILD, AFTER PARENT altered")

# This is said 'call super with arguments Child and self, then call the function altered on whatever it returns
dad = Parent3()
son = Child3()

dad.altered()
son.altered()

""" The reason for super()
- Multiple inheritance is when you define a class that inherits from one or more classes, like this:
    class SuperFun(Child, BadStuff):
        pass

- Python uses method resolution order (MRO) to look up which functions take priority and an algorithm C3 to get it straight.
"""

""" Using super() with __init__()
- The most common use of super() is actually in __init__ functions in base classes. So you do some things in the child, then complete
initialization in the parent.

class Child(Parent):

    def __init__(self, stuff):
        self.stuff = stuff
        super(Child, self).__init__()

- This is pretty much the same as the Altered Child example, except you're setting some variables in the __init__ before having the parent initialise with it's Parent.__init__

"""