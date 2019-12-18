# REFERENCE: COREY SCHAFER https://www.youtube.com/channel/UCCezIgC97PvUuR4_gbFUs5g

title = '''
Hello World!
This is string tutorial.
Enjoy'''
print(title)
print('-' * 20)

# BASIC STRING
string = 'Hello, this is a string: test!'
print(string)
print('-' * 20)

# STRING FORMATTING
print('Bobby\'s World')     # \ is a special character
print("Bobby's World")      # different types of quotes could be used
msg = '''
Multiple
Line
String
'''
print(msg)
first_name = 'John'
last_name = 'Smith'
msg = first_name + ' ' + last_name + ' wants an apple.'
print(msg)
msg = '{} {} wants an apple.'.format(first_name, last_name)     # Old python
print(msg)
msg = f'{first_name} {last_name} wants an apple.'               # New python: you could run code in placeholders!
print(msg)
print('-' * 20)

# USEFUL FUNCTIONS
string = 'Hello, this is a string: test!'
print(len(string))
print("Is the word 'Hello' in the string? " + str('Hello' in string))
print('-' * 20)

# CLASS STRING METHODS
string = 'Hello, this is a string: test!'
print(string.upper())
print(string.lower())
print(f"The letter 's appears {string.count('s')} times in the string")
print(f"The index of ':' is {string.find(':')}")
new_string = string.replace('a string', 'CODING')   # a new instance is necessary for the replacement
print(new_string)
print('-' * 20)

# STRING INDEXING
test_string = "Test String 0123 '!%@"
print(test_string)
print(test_string[0])
print(test_string[-1])
print(test_string[0:4])     # the first index is inclusive, the second one isn't
print(test_string[:4])      # from start to index 3
print(test_string[3:])      # from index 3 to the end
print('-' * 20)

# INPUT
name = input('What is your name? ')
print('Hello ' + name)
born_year = input('What year are you born into? ')
age = 2019 - int(born_year)
print('Well, you have ' + str(age) + ' years old!')
print('-' * 20)

# HELP
print(help(str))
