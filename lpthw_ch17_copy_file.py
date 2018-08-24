from sys import argv
from os.path import exists

script, from_file, to_file = argv

# I have turned the copy one file to another file script into one line!
# Note the difference between out_file and to_file. To_file might not exist prior to copy. 
out_file = open(to_file,'w').write(open(from_file).read())

