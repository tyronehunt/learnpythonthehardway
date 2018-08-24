# Usually a for loop is better than a while loop
# If you do use while, make sure it becomes False eventually
# When in doubt, print out the test variable at the top and bottom of the while loop to see what it's doing



def useless_number_function(num_input, num_variant):
    i = 0
    numbers = []

    while i < num_input: 
        print(f"At the top i is {i}")
        numbers.append(i)

        i = i + num_variant
        print("Numbers now: ", numbers)
        print (f"At the bottom i is {i}")

        print("The numbers: ")

    for num in numbers:
        print(num)

useless_number_function(5,2)
