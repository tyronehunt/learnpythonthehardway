# With lists you can only use number indexs to get things out of them. With dictionaries, you can use anything

# a dictionary is used to map or associate things (they're look up tables)
# a big thing dictionaries do not have is order!
# a list is an ordered list of items, whereas a dictionary is for matching items

stuff = {'name': 'Zed', 'age': 39, 'height':6 * 12 + 2}
print(stuff['name'])
print(stuff['age'])
print(stuff['height'])
stuff['city'] = 'SF'
print(stuff['city'])
stuff[1] = 'this actually goes at the end'
print (stuff)
del stuff['city']
del stuff[1]
print (stuff)

# create a mapping of state to abbreviation
states = {
    'Oregon': 'OR',
    'Florida':'FL',
    'California':'CA',
    'New York':'NY',
    'Michigan':'MI'
}

# create a basic set of states and some cities in them
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
print('-'*10)
print('NY State has: ', cities['NY'])
print('OR State has: ', cities['OR'])

# print some states
print('-'*10)
print("Michigan's abbreviation is: ", states['Michigan'])
print("Florida's abbreviation is: ", states['Florida'])

# do it by using the state then cities dict
print('-'*10)
print("Michigan has: ", cities[states['Michigan']])
print("Florida has: ", cities[states['Florida']])


# print every state abbreviation
print('-'*10)
for state, abbrev in list(states.items()):
    print(f"{state} state is abbreviated {abbrev}")
    print(f"and has city: {cities[abbrev]}")

print('-'*10)
# safely get an abbreviation by state that might not be there 
state = states.get('Texas')

if not state:
    print("Sorry, no Texas found")

# get a city with a default value
city = cities.get('TX','Does not exist')
print(f"The city for the state 'TX' is: {city}")
