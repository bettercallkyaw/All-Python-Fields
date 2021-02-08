# A List is a collection which is ordered and changeable. Allows duplicate members.

# Create list
fruits=['apple','orange','banana']
print(type(fruits),fruits)

# Use a constructor
fruits2=list(('apple','orange','banana'))
print(type(fruits2),fruits2)

# Get a value
print(fruits[0])

# Append to list
fruits.append('bluebarry')
print(fruits)

# Remove from list
fruits.remove('bluebarry')
print(fruits)

# Insert into a position
fruits[1]='redbarry'
print(fruits)

# Change Value
fruits[1]='orange'
print(fruits)

# Remove with pop
fruits.pop(2)
print(fruits)

# Reverse list
fruits.reverse()
print(fruits)

# Sort list
fruits.sort()
print(fruits)

# Reverse sort
fruits.sort(reverse=True)
print(fruits)
