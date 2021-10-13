# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string method

name='bob smith'
age=23

# Concatenate
print('hello my name is '+name+'.I am '+str(age)+' year old.')

# String Formatting

# Arguments by position
print('hello my name is {name}.I am {age} year old.'.format(name=name,age=age))

# F-Strings (3.6+)
print(f'hello my name is {name}.I am {age} year old.')

# String Methods
a='hello World'

# Capitalize string
print(a.capitalize())

# Make all uppercase
print(a.upper())

#Make all lowercase
print(a.lower())

# Swap case
print(a.swapcase())

# Get length
print(len(a))

# Replace
print(a.replace('hello','goodbye'))

# Count
sub='h'
print(a.count(sub))

# Starts with
print(a.startswith('h'))

#Ends with
print(a.endswith('d'))

# Split into a list
print(a.split())

# Find position
print(a.find('W'))

# Is all alphanumeric
print(a.isalnum())

# Is all alphabetic
print(a.isalpha())

# Is all numeric
print(a.isnumeric())