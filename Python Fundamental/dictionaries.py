# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

# Create dict
person={
    'fullName':'john doe',
    'email':'johndoe@gmail.com',
    'age':22,
    'city':'Boston'
}

print(type(person),person)

# Use constructor
person2=dict(fullName='robet peter',email='robet@gmail.com',age=33,city='San Fransecio')
print(type(person2),person2)

# Get value
print(person['fullName'])
print(person2.get('email'))
print(person2['city'])

# Add key/value
person['phone']=934567898
print(person)

# Get dict keys
print(person.keys())

# Get dict items
print(person.items())

# Copy dict
person2=person.copy()
person2['city']='yangon'
print(person2)

# Remove item
del(person['phone'])
print(person)

#Remove with pop
person.pop('age')
print(person)

# Clear
person.clear()
print(person)

# Get length
print(len(person2))

# List of dict
people=[
    {
        'name':'william smith',
        'email':'william@gmail.com',
        'age':22,
        'city':'london'
    },
    {
        'name':'bob nathan',
        'email':'bob@gmail.com',
        'age':44,
        'city':'berlin'
    }
]

print(type(people))
print(people)
print(people[0]['email'])