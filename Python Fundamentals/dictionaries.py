# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

# Create dict

person={
    "fullName":"bob smith",
    "email":"bob@gmail.com",
    "city":"boston",
    "age":23
}

print(type(person),person)

# Use constructor
person1=dict(fullName="john smith",email="john@yahoo.com",city="london",age=34)
print(type(person1),person1)

# Get value
print(person["fullName"])
print(person1.get("city"))
print(person1["age"])

# Add key/value
person["job"]="teacher"
print(person)

# Get dict keys
print(person.keys())

# Get dict items
print(person.items())

# Copy dict
person1=person.copy()
person1["city"]="berlin"
print(person1)

# Remove item
del(person["job"])
print(person)

#Remove with pop
person.pop("email")
print(person)

# Clear
person.clear()
print(person)

# Get length
print(len(person1))

# List of dict
people=[
    {
        "fullName":"robet Peter",
         "job":"developer",
         "hobbies":["sports","movies","guitar"],
         "email":"robet@gmail.com",
         "age":23
    },
    {
        "fullName":"william",
        "job":"designer",
        "email":"william@gmail.com",
        "age":44
    }
]

print(type(people),people)
print(people[0]["fullName"])
print(people[0]["hobbies"][1])
print(people[1]["email"])