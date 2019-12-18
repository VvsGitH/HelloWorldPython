title = '''
Hello World!
This is a basic program.
Enjoy'''
print(title)
print('-' * 20)
name = input('What is your name? ')
print('Hello ' + name)
born_year = input('What year are you born into? ')
age = 2019 - int(born_year)
print('Well, you have ' + str(age) + ' years old!')

title = '''
Python Indexing'''
print(title)
print('-' * 20)
test_string = "Test String 0123 '!%@"
print(test_string)
print(test_string[0])
print(test_string[-1])
print(test_string[0:4])
print(test_string[1:-1])

title = '''
String Formatting'''
print(title)
print('-' * 20)
first_name = 'John'
last_name = 'Smith'
msg = f'{first_name} [{last_name}] wants an apple.'
print(msg)
print(f'This string is {len(msg)} character long!')

title = '''
String Class Methods'''
print(title)
print('-' * 20)
string = 'Hello, this is a string: test!'
print(string.upper())
print(string.lower())
print(f"The index of ':' is {string.find(':')}")
print(string.replace('a string', 'CODING'))
print("Is the word 'Hello' in the string? " + str('Hello' in string))
