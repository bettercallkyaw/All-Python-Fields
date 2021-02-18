# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

# Create class
class User:
    # Constructor
      def __init__(self,name,email,age):
          self.name=name
          self.email=email
          self.age=age

      def greeting(self):
          return f'Hello My name is {self.name}.I am {self.age} year old.'     
      
      def has_birthday(self):
          self.age+=1
#Extend Class
class Customer(User):   
    # Constructor
       def __init__(self,name,email,age):
           self.name=name
           self.email=email
           self.age=age
           self.balance=0

       def set_balance(self,balance):
            self.balance=balance 

       def greeting(self):
          return f'Hello My name is {self.name}.I am {self.age} year old.My balance is {self.balance}'       
      

# init user object
john=User('john doe','john@gmail.com',22)
print(type(john))
print(john.name)
john.has_birthday()
print(john.greeting())

# init customer object
robet=Customer('robet','robet@gmail.com','33')
robet.set_balance(900)
print(robet.greeting())