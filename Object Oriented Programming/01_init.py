class User:
    def __init__(self,first,last,age):
        self.first=first 
        self.last=last
        self.age=age

user1=User('Robet','Peter',22)
user2=User('John','Smith',25)
print(user1.first,user2.last)
print(user2.first,user2.last)            