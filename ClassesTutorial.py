# REFERENCE: COREY SCHAFER https://www.youtube.com/channel/UCCezIgC97PvUuR4_gbFUs5g
# ---- INCOMPLETE ----

import copy     # Importing library


class Person:       # No need to define attributes
    def __init__(self, name, age):      # Constructor
        self.name = name        # self argument refers to the object that call the function: like this-> in C++
        self.age = age

    def __str__(self):      # Overloading casting-operator str
        return 'Mr/s ' + str(self.name) + '\n' + '   ' + 'Age: ' + str(self.age)


class Point:
    def __init__(self, x=0, y=0, z=0):      # Initializing coordinates with zeros; x,y,z are now optional arguments
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f'({self.x}, {self.y}, {self.z})'

    def __add__(self, p):       # Overloading operator +
        return Point(self.x + p.x, self.y + p.y, self.z + p.z)

    def __mul__(self, p):       # Overloading operator * between two Point objects
        return self.x * p.x + self.y * p.y + self.z * p.z

    def __rmul__(self, s):      # Overloading operator * between Point object and other variables
        return Point(self.x * s, self.y * s, self.z * s)


title = '''
Hello World!
This is classes tutorial.
Enjoy'''
print(title)
print('-' * 20)

my_name, my_age = input('Write down your full name: '), input('Write down your age: ')      # Multiple variables init
pers = Person(my_name, my_age)      # Object declaration and initialization
print(pers)     # print function with only the object as argument does an hidden call of str casting-operator

p1 = Point(3, 2)        # not using z arguments means leaving z-coordinate at 0
print(p1)
p1_copy = copy.copy(p1)     # copying the object into another object
p2 = p1     # copying object and object-pointer
print('Is p1_copy the same object as p1? ' + str(p1_copy == p1))
print('Is p2 only an alias of p1 (same object but different name)? ' + str(p2 == p1))


