# REFERENCE: Socratica - https://www.youtube.com/channel/UCW6TXMZ5Pq6yL6_k5NZ2e0Q

from functools import lru_cache


# HELLO FUNCTION
def hello_function():
    """ function description """
    title = '''
    Hello World!
    This is a function tutorial.
    Enjoy'''
    print(title)


# SIMPLE FUNCTION WITH INPUT CHECK
def basic_func(a, b):
    """ linear combination y = 2a + 3b """
    # Check the input for data type
    if type(a) not in [int, float]:
        raise TypeError("n must be a positive integer")
    return 2*a + 3*b


# FUNCTION WITH DEFAULT (OR KEYWORD) ARGUMENTS
def cm(feet=0, inches=0):
    """ converts a length from feet and inches to centimeters"""
    inches_to_cm = inches * 2.54
    feet_to_cm = feet * 12 * 2.54
    return inches_to_cm + feet_to_cm


# RECURSIVE FUNCTION WITH MEMOIZATION
@lru_cache(maxsize=1000)    # this is a decorator: it enables caching for the function
def fibonacci_sequence(n):
    """ return the Nth element of the Fibonacci Sequence (starting from 0) """
    # Check the input for data type
    if type(n) != int:
        raise TypeError("n must be a positive integer")
    if n < 1:
        raise ValueError("n must be at least 1")
    # Compute the Nth term
    if n == 1:
        return 0
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacci_sequence(n-1) + fibonacci_sequence(n-2)


# LAMBDA EXPRESSIONS
# lambda x1, x2, ..., xn: <expression>
# common functions could return lambda expressions
#   Application 1 : Give them a name and use them as functions (not very used)
""" Eg1 - Composing the full name from distinct and badly written first and last name """
def full_name(first, last): return first.strip().title() + " " + last.strip().title()


print('Full Name =', full_name('     vito', '  PAPARELLA   '))


""" Eg2 - Calculating the value of a polynomial expression """
def value(x): return 2*x**2 + 3*x - 5


print("The polynomial '2x^2 + 3x -5' in x=0 is equal to:", value(0))


#   Application 2 : Use them in the key of a sort functions
name_list = ['Vito Paparella', 'Gino Pauli', 'Rocco Lollo', 'Pinco Pallo', 'Beppe Freppe']
name_list.sort(key=lambda name: name.split(" ")[0])         # Ordering by name
print(name_list)
name_list.sort(key=lambda surname: surname.split(" ")[-1])  # Ordering by surname
print(name_list)


# MAP FUNCTION
# Iterate a function over a list of inputs
# Data: a1, a2, ..., an
# Function: f
# map(f, data) = [f(a1), f(a2, ..., f(an)]
# map return a map_object that could be converted into a list
""" Eg1 - Returning selected values of the Fibonacci Sequence without a loop """
indexes = [1, 5, 10, 100]
fibonacci_values = map(fibonacci_sequence, indexes)
print(list(fibonacci_values))
""" Eg2 - Converting temperatures from Celsius of Fahrenheit in a series of tuples """
temps = [("Los Angeles", 25), ("Tokyo", 27), ("New York", 28), ("London", 22), ("Beijing", 32)]
temps_fahrenheit = map(lambda data: (data[0], 9/5*data[1]+32), temps)   # F = 9/5*C +32
print(list(temps_fahrenheit))


# FILTER FUNCTION
# Filters a set of data with a defined condition
# return a filter_object
""" Eg1 - remove empty elements of a list"""
test_list = ['elm1', '', 'elm2', 'elm3', '', '', 'elm4']
clean_list = filter(None, test_list)
print(list(clean_list))
""" Eg2 - filter away all the data above the average """
data = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]
avg = sum(data)/len(data)
above_avg_data = filter(lambda x: x > avg, data)
print(list(above_avg_data))
