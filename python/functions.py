def greet():
    '''dispalying hi function'''
    print('hi')
greet()

def greet(name):
   
    print('hi',name)

greet("akshat")
greet("sir")

"""
positional argument
def greet(name,city):
    print(f'welcome {name} to the {city}')

greet(raju,mumbai)


keyword argument
greet(name="raju",city="mumbai")

default argument
def greet(name="raju",city="mumbai"):
    print(f'welcome {name} to the {city}')

greet()
greet(name="sagar",city="delhi")
"""