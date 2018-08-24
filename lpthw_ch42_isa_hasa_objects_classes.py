# A class and an object are the same thing at different points in time
# A fish is a class, it's a word we attach to instances of things with similar attributes
# A salmon is also a class, but with more specific attributes (longer nose, red flesh etc.)
# Naming a particular fish Mary is an instance of a salmon, and also an instance of a fish - but it's also an object

""" You use the phrase 'is-a' when you talk about objects and classes being related to each other by a class relationship
You use the phrase 'has-a' is when you talk about objects and classes that are related only because they reference each other
--> is-a is the relationship between salmon and fish, whereas has-a is the relationship between salmon and gills
"""

## Animal is-a object (yes, sort of confusing)
class Animal(object):
    pass

## Dog is-a animal, that has-a __init__ that takes self and name parameters
class Dog(Animal):
    def __init__(self, name):
        ## ??
        self.name = name

## Cat is-a animal, that has-a __init__ that takes self and name parameters
class Cat(Animal):
    def __init__(self, name):
        ## ??
        self.name = name

## Person is-a object that has-a __init__ that takes self and name.
class Person(object):
    def __init__(self, name):
        ## Person has-a name of some kind
        self.name = name
        ## Person has-a pet of some kind
        self.pet = None

## Employee is a Person, that has-a __init__ that takes self, name and salary parameters
class Employee(Person):
    def __init__(self, name, salary):
        # this is how you run the __init__ method of a parent class reliably
        super(Employee, self).__init__(name)
        # Employee has a salary of some kid
        self.salary = salary

## Fish is an object
class Fish(object):
    pass

## Salmon is-a Fish
class Salmon(Fish):
    pass

## Halibus is-a Fish
class Halibut(Fish):
    pass

# rover is a Dog
rover = Dog("Rover")

# Satan is a Cat
satan = Cat("Satan")

# Mary is a person
mary = Person("Mary")

# Mary has a pet set to satan
mary.pet = satan

# frank is an instance of Employee with name Frank and salary 120000
frank = Employee("Frank", 120000)

# frank has a pet set to rover
frank.pet = rover

# flipper is an instance of Fish
flipper = Fish()

# crouse is an instance of Salmon
crouse = Salmon()

# harry is an instance of Halibut
harry = Halibut()

""" CODECADEMY CLASS INHERTIANCE EXAMPLE"""
class Staff(object):
    def __init__(self, employee_name):
        self.employee_name = employee_name

    def calculate_wage(self, hours):
        self.hours = hours
        return hours * 20.00


class PartTimeEmployee(Staff):
    def calculate_wage(self, hours):
        self.hours = hours
        return hours * 12.00
  
    def full_time_wage(self, hours):
        self.hours = hours
        # Use the super function to call upon the parent class (Staff) and use its function calculate_wage
        # Note in Python3, you could just do super().calculate_wage(hours)
        return super(PartTimeEmployee, self).calculate_wage(hours)

milton = PartTimeEmployee('Milton')
print(milton.calculate_wage(10))
print (milton.full_time_wage(10))