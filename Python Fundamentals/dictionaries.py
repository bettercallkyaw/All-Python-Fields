# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

# Create dict
person1={
    'name':'bob smith',
    'email':'bob@gmail.com',
    'city':'boston',
    'age':22
}

print(type(person1),person1)

# Use constructor
person2=dict(name='john doe',email='john@gmail.com',city='london',age=25)
print(type(person2),person2)

# Get value
print(person1['name'])
print(person1.get('email'))
print(person2['city'])

# Add key/value
person1['job']='developer'
print(person1)

# Get dict keys
print(person1.keys())

# Get dict items
print(person1.items())

# Copy dict
person2=person1.copy()
person2['city']='berlin'
print(person2)

# Remove item
del(person1['job'])
print(person1)

#Remove with pop
person1.pop('email')
print(person1)

# Clear
person1.clear()
print(person1)

# Get length
print(len(person2))

# List of dict
people=[
    {
        'name':'jack peter',
        'hobbies':['hiking','movies','sports'],
        'facebook':'www.facebook.com/profile.php?id=6789'
    },
    {
         'name':'jemi jack',
         'hobbies':['bass guitar','coding','music'],
         'twitter':'www.twitter.com/@jemi34'
    }
]

print(type(people),people)
print(people[0]['name'])
print(people[1]['hobbies'][2])