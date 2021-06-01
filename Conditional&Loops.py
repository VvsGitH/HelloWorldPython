# REFERENCE: COREY SCHAFER https://www.youtube.com/channel/UCCezIgC97PvUuR4_gbFUs5g

title = '''
Hello World!
This is a tutorial on IF statements and loops.
Enjoy'''
print(title)
print('-' * 20)

# BASIC IF STATEMENT
condition = True
if condition:
    print('The condition is fulfilled')
else:
    print('The condition in unfulfilled')
print('-' * 20)

# FALSE CONDITIONS
#   False
#   None
#   0, '', [], {}

# IF STATEMENT AS SWITCH CASE
a = input('Input case (1 to 3): ')
if a == '1':
    print('You selected case 1')
elif a == '2':
    print('You selected case 2')
elif a == '3':
    print('You selected case 3')
else:
    print('Default case')
print('-' * 20)


# BASIC FOR LOOP
for i in range(2, 5):       # loop for incremental i values between 2 and 4
    print(i)

nums = [1, 2, 3, 4, 5]
print(nums)
for num in nums:            # loop over the element of the vector
    print(num)

print('-' * 20)

# CONDITIONAL FOR LOOP
for num in nums:
    if num == 3:
        print('Found 3!')
        break               # exit from the loop when condition is true
    print('searching')

for num in nums:
    if num == 3:
        print('Found 3!')
        continue            # skip to the next iteration when condition is true
    print(num)

print('-' * 20)


# WHILE LOOP
x = 0
while x < 4:                # loop until condition is satisfied
    print(x)
    x += 1

x = 0
while True:                 # infinite loop -> CTRL+C to exit if something goes wrong
    if x == 5:
        break
    print('searching')
    x += 1
