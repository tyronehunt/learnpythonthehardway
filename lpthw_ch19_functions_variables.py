# Variables in your script are not linked to variables in your functions
# Note it's best practice to have diferent function names for defining your function and for the variables you pass into them

def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses")
    print(f"You have {boxes_of_crackers} boxes of crackers")
    print("Get a blanket. \n")

print("We can just give the function numbers directly: ")
cheese_and_crackers(20,30)

print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese,amount_of_crackers)

print("We can even do maths inside too:")
cheese_and_crackers(10+20, 5+6)

print("And we can combine variables and maths inside functions: ")
cheese_and_crackers(amount_of_cheese+20, amount_of_crackers+30)