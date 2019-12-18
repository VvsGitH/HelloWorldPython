# REFERENCE: COREY SCHAFER https://www.youtube.com/channel/UCCezIgC97PvUuR4_gbFUs5g

title = '''
Hello World!
This is numbers tutorial.
Enjoy'''
print(title)
print('-' * 20)

# NUMBER TYPES
n = 3
print(n, ' is a ', type(n))
n = 3.14
print(n, ' is a ', type(n))
print('-' * 20)

# OPERATORS
#   Addiction:      a + b
#   Subtraction:    a - b
#   Multiplication: a * b
#   Exponential:    a ** b
#   Division:       a / b
#   Floor Division: a // b
#   Remainder:      a % b

# COMPARISONS
#   Equal:          a == b
#   Not Equal:      a != b
#   Greater/Equal:  a >= b
#   Less/Equal:     a <= b

# INCREMENT
n = 1
n += 1
print(n)
print('-' * 20)

# USEFUL FUNCTIONS
n = -34
print(abs(n))
n = 3.456
dec = 2
print(round(n, dec))     # Round to the 2nd decimal
print('-' * 20)

# CASTING
n1 = '100'
n2 = '112.3'
n = int(n1) + float(n2)
print(n)
n = float(n1) + float(n2)
print(n)        # The result is the same, Python doesn't care about summing integer and float
