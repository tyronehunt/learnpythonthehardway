# Import the arguments module from sys package
from sys import argv

# Import the exists module from path package on MAC OS
from os.path import exists

# This script takes 3 arguments
script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

# open the file to copy from, read the contents and store them in a variable
indata = open(from_file).read()

# Output how many characters are in the input file
print(f"The input file is {len(indata)} bytes long")

# Check whether the output file exists - True or False (if it doesn't, script just creates it)
print(f"Does the output file exist? {exists(to_file)}")

# This line is completely unnecessary to be honest - maybe as a safe check
print("Ready, hit RETURN to continue, CTRL-C to abort. ")
input()

# Opens the file to write to (whether it exists or not)
out_file = open(to_file,'w').write(indata)

print ("All done!")

# Note you would usually close your script here, but if you've run a method on an opened file in one line, the script will automatically close