# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

# Create tuple
fruits1=('apple','banana','orange')
print(type(fruits1),fruits1)

# Using a constructor
fruits2=tuple(('apple','banana','orange'))
print(type(fruits2),fruits2)

# Single value needs trailing comma
fruits3=('apple',)
print(type(fruits3),fruits3)

# Get value
print(fruits1[1])

# Can't change value
# fruits1[0]='mango'
# print(fruits1)

# Delete tuple
# del fruits1
# print(fruits1)

# Get length
print(len(fruits1))

# A Set is a collection which is unordered and unindexed. No duplicate members.

# Create set
fruits_set={'apple','banana','orange'}

# Check if in set
if 'apple' in fruits_set:
    print('apple' in fruits_set)

# Add to set
fruits_set.add('mango')
print(fruits_set)

# Remove from set
fruits_set.remove('mango')
print(fruits_set)

# Add duplicate
fruits_set.add('apple')
print(fruits_set)

# Clear set
# fruits_set.clear()
# print(fruits_set)

# Delete set
del fruits_set
print(fruits_set)