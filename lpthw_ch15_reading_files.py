from sys import argv
#Import arguments module from sys package

# set the arguments for running the python file
script, filename = argv

# open a text file (passed in from argv) and set it equal to a variable named txt
txt = open(filename)

# use the .read() method to print the contents of the text file
print(f"Here's your file {filename}: ")
print (txt.read())

# now look how the same thing can be achieved with input, rather than argv
print("Type the filename again: ")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())
