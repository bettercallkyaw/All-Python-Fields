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
fruits.append('redbarry')
print(fruits)

# Remove from list
fruits.remove('redbarry')
print(fruits)

# Insert into a position
fruits[0]='mango'
print(fruits)

# Change Value
fruits[0]='apple'
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
fruits.sort(reverse=False)
print(fruits)
