from sys import argv

script, filename = argv

# Makek sure you always open the file first before trying to do anything with it. Also the r or w must be a 'r' or 'w'
opened_file = open(filename, 'w')

# Note you can't just call the .read() method on it's own, you'll need to then pring that to the terminal, ideally through a variable medium
# Also note that you can't call .read() if you've selected 'w' mode when opening the file
# file_contents = opened_file.read()

# This text updates the opened file
opened_file.write("This should override any text, making the truncate() method redundant to be honest")

# Now I want to read it, so should close it first, then open again with read mode
opened_file.close()

# Note, if you try to put opened_file in as the parameter it won't work, because that variable name has already been designated as 'w'
opened_file_2 = open(filename)

# Note, I didn't bother with the variable medium this time for seeing what I'd done to the file
print(opened_file_2.read())

print(f"Congrats, you just successfully updated the file: {filename}")

