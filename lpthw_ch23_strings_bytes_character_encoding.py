# Note up until now have been saying 'from sys import argv'. This time we're importing everything, hence the need for sys.argv
import sys
script, encoding, error = sys.argv

def main(language_file, encoding, errors):
    line = language_file.readline()
    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, error)

def print_line(line, encoding, errors): 
    next_lang = line.strip()
    raw_bytes = next_lang.encode(encoding, errors=errors)
    cooked_string = raw_bytes.decode(encoding, errors=errors)

    print(raw_bytes, "<===>", cooked_string)

languages = open("lpthw_ch23_test.txt", encoding="utf-8")

main(languages, encoding, error)