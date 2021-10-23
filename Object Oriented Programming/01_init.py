class User:
    def __init__(self,first,last,age):
        self.first=first
        self.last=last
        self.age=age

user1=User('bob','smith',23)
user2=User('john','doe',30)
print(type(user1))
print(user1.first,user1.last)
print(user2.first,user2.last)