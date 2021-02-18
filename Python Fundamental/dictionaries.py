# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

# Create dict
person={
    'fullName':'Robet Peter',
    'email':'robet@gmail.com',
    'age':22,
    'city':'Boston'
}

print(type(person),person)

# Use constructor
person2=dict(fullName='John Smith',email='john@gmail.com',age=33,city='New York')
print(type(person2),person2)

# Get value
print(person['fullName'])
print(person2.get('fullName'))
print(person2['email'])

# Add key/value
person['phone']=999234567
print(person)

# Get dict keys
print(person.keys())

# Get dict items
print(person.items())

# Copy dict
person2=person.copy()
person2['city']='Yangon'
print(person2)

# Remove item
del(person['phone'])
print(person)

#Remove with pop
person.pop('fullName')
print(person)

# Clear
person.clear()
print(person)

# Get length
print(len(person2))

# List of dict
people=[
    {
        'name':'William Smith',
        'email':'william@gmail.com',
        'city':'London',
        'age':22
    },
    {
        'name':'Bob Kate',
        'email':'bob@gmail.com',
        'city':'Berlin',
        'age':25
    }
]

print(type(people),people)
print(people[0]['name'])