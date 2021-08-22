# A List is a collection which is ordered and changeable. Allows duplicate members.

# Create list
fruits=["apple","orange","banana"]
print(type(fruits),fruits)

# Use a constructor
fruits1=list(("apple","orange","banana"))
print(type(fruits1),fruits1)

# Get a value
print(fruits[0])

# Append to list
fruits.append("redbarry")
print(fruits)

# Remove from list
fruits.remove("redbarry")
print(fruits)

# Insert into a position
fruits[0]="greenbarry"
print(fruits)

# Change Value
fruits[0]="apple"
print(fruits)

# Remove with pop
fruits.pop(0)
print(fruits)

# Reverse list
fruits1.reverse()
print(fruits1)

# Sort list
fruits1.sort()
print(fruits1)

# Reverse sort
fruits1.sort(reverse=True)
print(fruits1)