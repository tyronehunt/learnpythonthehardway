"""
.close() - closes the file
.read() - reads the contents of a file
.readline() - reads just one line of a text file
.truncate() - empties the file!
.write('stuff') - writes "stuff" to the file
.seek(0) - moves read/write location to the beginning of the file
"""

# From sys package import argv module
from sys import argv

# The import argument is a filename
script, filename = argv

# Some basic go / no-go on deleting code
print(f"We're going to erase {filename}.")
print ("If you don't want that, hit CTRL - C (^C). ")
print("If you do want that, hit RETURN.")

input("?")

# Open the argument filename for writing
print("Opening the file...")
target = open(filename, 'w')

# Delete the contents of the opened file - ouch!
print("Truncating the file. Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines")

# Get content to write to the empty, opened file
line1 = input("Line 1: ")
line2 = input("Line 2: ")
line3 = input("Line 3: ")

print("I'm going to write these to the file. ")

# Write that 'stuff' in there! (Note my snazzy use of strings, formats and escapes)
target.write(f"{line1} \n{line2} \n{line3} \n")

print("And finally, we close it.")
target.close()