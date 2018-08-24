"""
class - tell Python to make a new type of thing
object - the most basic type of thing and any instance of some thing
instance - what you get when you tell python to create a class
def - how you define a function inside a class
self - inside the functions in a class, self is a variable for the instance/object being accessed
inheritance - one class can inherit traits from another
composition - a class can be composed of other classes as parts, much like how a car has wheels
attribute - a property classes have that are from composition and are usually variables
is-a - phrase to say something inherits from another (salmon is a fish)
has-a - phrase to say something is composed of other things or has a trait, as in (salmon has a mouth)

class X(Y) - make a class named X that is-a Y
class X(object): def__init__(self, J) - class X has-a __init__ that takes self and J parameters
class X(object): def M(self, J) - class X has-a function named M that takes self and J parameters
foo = X() - set foo to an instance of class X
foo.M(J) - from foo, get the M function and call it with parameters self and J
foo.K = Q - from foo, get the K attribute and set it to Q
"""

import random
from urllib.request import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

PHRASES = {
    "class %%%(%%%):":
    "Make a class named %%% that is-a %%%.",
    "class %%%(object):\n\tdef __init__(self, ***)":
    "class %%% has-a __init__ that takes self and *** params",
    "class %%%(object):\n\tdef ***(self, @@@)":
    "class %%% has-a function *** that takes self and @@@ params.",
    "*** = %%%()":
    "Set *** to an instance of class %%%.",
    "***.***(@@@)":
    "From *** get the *** function, call it with params self, @@@.",
    "***.*** = '***'":
    "From *** get the *** attribute and set it to '***'."
}

#do they want to drill phrases first
if len(sys.argv) == 2 and sys.argv[1] == "english":
    PHRASE_FIRST = True
else:
    PHRASE_FIRST = False

#load up the words from the website
for word in urlopen(WORD_URL).readlines():
    WORDS.append(str(word.strip(), encoding="utf-8"))

def convert(snippet, phrase):
    class_names = [w.capitalize() for w in
    random.sample(WORDS, snippet.count("%%%"))]
    other_names = random.sample(WORDS, snippet.count("***"))
    results = []
    param_names = []

    for i in range(0, snippet.count("@@@")):
        param_count = random.randint(1,3)
        param_names.append(', '.join(
            random.sample(WORDS, param_count)))
    
    for sentence in snippet, phrase:
        # slice from very first element to very last one - effectively copies the list
        result = sentence[:]

        # fake class names
        for word in class_names:
            result = result.replace("%%%",word, 1)

        # fake other names
        for word in other_names:
            result = result.replace("***", word, 1)

        # fake parameter lists
        for word in param_names:
            result = result.replace("@@@", word, 1)

        results.append(result)
    return results

# keep going until they hit CTRL-D
try: 
    while True:
        snippets = list(PHRASES.keys())
        random.shuffle(snippets)

        for snippet in snippets:
            phrase = PHRASES[snippet]
            question, answer = convert(snippet, phrase)
            if PHRASE_FIRST:
                question, answer = answer, question

            print(question)

            input("> ")
            print(f"ANSWER: {answer}\n\n")
except EOFError:
    print("\nBye")