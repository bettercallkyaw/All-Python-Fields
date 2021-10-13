# A List is a collection which is ordered and changeable. Allows duplicate members.

# Create list
fruits1=['apple','banana','orange']
print(type(fruits1),fruits1)

# Use a constructor
fruits2=list(('apple','banana','orange'))
print(type(fruits2),fruits2)

# Get a value
print(fruits1[0])

# Append to list
fruits1.append('mango')
print(fruits1)

# Remove from list
fruits1.remove('mango')
print(fruits1)

# Insert into a position
fruits1[0]='mango'
print(fruits1)

# Change Value
fruits1[0]='apple'
print(fruits1)

# Remove with pop
fruits1.pop(0)
print(fruits1)

# Reverse list
fruits2.reverse()
print(fruits2)

# Sort list
fruits2.sort()
print(fruits2)

# Reverse sort
fruits2.sort(reverse=True)
print(fruits2)