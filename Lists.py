# REFERENCE: COREY SCHAFER https://www.youtube.com/channel/UCCezIgC97PvUuR4_gbFUs5g

title = '''
Hello World!
This is lists tutorial.
Enjoy'''
print(title)
print('-' * 20)

# CREATING A LIST
lst = []                            # Empty List
print(lst)
lst = ['Elm1', 'Elm2', 'Elm3']      # String List
print(lst)
print('-' * 20)

# ELEMENTS OF A LIST
print(lst[0])           # First element
# indexing is the same as strings
lst.append('Elm4')      # Add an element to the end
print(lst)
lst.remove('Elm2')      # Remove an element
print(lst)
lst.insert(1, 'Elm2')   # Insert an element in index 1
print(lst)
lst2 = ['Elm5', 'Elm6']
lst.append(lst2)        # Insert lst2 as an unique element
print(lst)
lst.remove(lst2)
lst.extend(lst2)        # Insert the elements of lst2 in lst
print(lst)
popped = lst.pop()      # Remove the last element and puts it into popped
print(popped, lst)
print('-' * 20)

# USEFUL FUNCTIONS
lst = ['a', 'c', 'e', 'b']
print(len(lst))                 # Number of elements
sort_lst = sorted(lst)          # Generated a new sorted list
print(sort_lst)
print(lst.sort())               # Sort in place in alphabetical or numerical Order
print(lst.sort(reverse=True))   # Reverse sorting
print('d' in lst)               # Check if 'd' is in the list
print('-' * 20)

# VECTORS
v = [1, 3, 6, 10, 12]
print(v)
print(min(v))
print(max(v))
print(sum(v))
print('-' * 20)

# FOR LOOPS
lst = ['Elm1', 'Elm2', 'Elm3']
for elm in lst:                             # loop over the elements of the list
    print(elm)
for ind, elm in enumerate(lst):             # loop over elements and indexes
    print(ind, elm)
for ind, elm in enumerate(lst, start=1):    # loop over elements and indexes, starting from 1
    print(ind, elm)
print('-' * 20)

# TRANSFORMING INTO STRINGS
separator = ', '                    # separation characters between elements
lst_str = separator.join(lst)       # put all elements in one string
print(lst_str)
new_lst = lst_str.split(separator)  # split the string into a list
print(new_lst)
print('-' * 20)

# TUPLES
# Immutable data types: cannot be modified after creation
tpl = ()
print(tpl)
tpl = ('a', 'b', 'c')
print(tpl)



