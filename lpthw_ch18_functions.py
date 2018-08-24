# This function is like scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

# Ok, the *args is actually pointless, you can just do this
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

# This function doesn't take any arguments!
def print_none():
    print("I got nothing!")

print_two("Tye","Hunt")
print_two_again("Tye","Hunt")
print_none()