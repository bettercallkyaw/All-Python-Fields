# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

# Create class
class User:
    #Constructor
    def __init__(self,name,email,age):
        self.name=name
        self.email=email
        self.age=age

    def greeting(self):
        return f'hello my name is {self.name}.I am {self.age} year old.'  

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
        return f'hello my name is {self.name}.I am {self.age} year old.My balance is {self.balance}.'      

user=User('bob smith','bob@gmail.com',22)
print(type(user))
print(user.name)
user.has_birthday()
print(user.greeting())

customer=Customer('william smith','william@gmail.com',25)
print(type(customer))
print(customer.name)
customer.set_balance(999)
print(customer.greeting())