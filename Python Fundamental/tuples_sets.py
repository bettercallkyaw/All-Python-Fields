# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

# Create tuple
fruits=('apple','orange','banana')
print(type(fruits),fruits)


# Using a constructor
fruits2=tuple(('apple','orange','banana'))
print(type(fruits2),fruits2)

# Single value needs trailing comma
fruits3=('apple',)
print(fruits3,type(fruits3))

# Get value
print(fruits[0])

# Can't change value
# fruits[1]='redbarry'
# print(fruits)

# Delete tuple
# del fruits
# print(fruits)

# Get length
print(len(fruits3))

# A Set is a collection which is unordered and unindexed. No duplicate members.


# Create set
fruits_set={'apple','orange','banana'}

# Check if in set
print('apple' in fruits_set)

# Add to set
fruits_set.add('bluebarry')
print(fruits_set)

# Remove from set
fruits_set.remove('bluebarry')
print(fruits_set)


# Add duplicate
fruits_set.add('apple')
print(fruits_set)

# Clear set
# fruits_set.clear()
# print(fruits_set)

# Delete set
# del fruits_set
# print(fruits_set)