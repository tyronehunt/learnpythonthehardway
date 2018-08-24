# Inheritance is useful, but you can do the exact same thing by using other classes and modules
# Rather than with inheritance where Child is-a Parent, we now have Child has-a Other
# Note how you have to initialise an instance of a Child class, but after that you can call the functions from Other on it (this could be a Class or a module)

class Other(object):

    def override(self):
        print("OTHER override()")

    def implicit(self):
        print("OTHER implicit()")

    def altered(self):
        print("OTHER altered")

class Child(object):

    def __init__(self):
        self.other = Other()

    def implicit(self):
        self.other.implicit()

    def override(self):
        self.other.override()

    def altered(self):
        print ("CHILD, BEFORE OTHER altered()")
        self.other.altered()
        print ("CHILD, AFTER OTHER altered()")

son = Child()

son.implicit()
son.override()
son.altered()

""" INHERITANCE VS COMPOSITION
- Avoid multiplie inheritance at all costs - if you do use it, spend the time to work out where things are coming from and their priorities
- Use composition to package code into modules that are used in many different unrelated places / situations
- Use inheritance only when there are clearly related reusable pieces of code that fit under a single common concept
"""

