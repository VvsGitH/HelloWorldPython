# REFERENCE: COREY SCHAFER https://www.youtube.com/channel/UCCezIgC97PvUuR4_gbFUs5g

title = '''
Hello World!
This is dictionaries tutorial.
Enjoy'''
print(title)
print('-' * 20)

# CREATING DICTIONARIES
new_dictionary = {}                                         # empty dictionary
print(new_dictionary)
student = {'name': 'John', 'age': 25, 'courses': [
    'Math', 'Algebra']}   # initialized dictionary
print(student)

# MODIFYING DICTIONARIES
new_dictionary['new_key'] = 'new_word'                      # adding key and value
print(new_dictionary)
new_dictionary.update({'new_key': 3, 'key2': 'value'})      # updating and/or adding values
print(new_dictionary)
del new_dictionary['key2']                                  # deleting keys
print(new_dictionary)

# PRINT WORDS
print(student['age'])               # returns the value corresponding to the key
print(student.get('age'))           # the same, but returns None in case of key not existent
print(student.get('address'))

# PRINT ALL KEYS AND VALUES
print(student.keys())       # all the keys
print(student.values())     # all the values
print(student.items())      # all the keys and values
for key, word in student.items():   # for loop technique
    print(key, word)
