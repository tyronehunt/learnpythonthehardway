formatter = "{} {} {} {}"

print (formatter.format(1,2,3,4))
print (formatter.format("one","two","three","four"))
print (formatter.format(True,False,True,False))
print (formatter.format(formatter,formatter,formatter,formatter ))

print(formatter.format(
    "The owl",
    "and the",
    "pussy cat",
    "went out to sea"
))