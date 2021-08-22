# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

# Create class
class User:
    #Constructor
    def __init__(self,name,email,age):
        self.name=name
        self.email=email
        self.age=age

    def greeting(self):
        return f"Hello My name is {self.name} and I am {self.age} year old."

    def has_birthday(self):
        self.age+=1

#Extend class
class Customer(User):
    def __init__(self,name,email,age):
        self.name=name
        self.email=email
        self.age=age
        self.balance=0

    def set_balance(self,balance):
        self.balance=balance

    def greeting(self):
        return f'Hello My name is {self.name} and I am {self.age} year old.My balance is {self.balance}.' 


bob=User("bob smith","bob@gmail.com",23)
print(type(bob))
print(bob.name)
bob.has_birthday()
print(bob.greeting())

robet=Customer("robet peter","robet@gmail.com",34)
print(type(robet))
robet.set_balance(900)
print(robet.greeting())