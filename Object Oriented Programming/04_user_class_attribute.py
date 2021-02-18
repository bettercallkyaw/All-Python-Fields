# A User class with both a class attribute
class User:

    active_users=0

    def __init__(self,first,last,age):
        self.first=first 
        self.last=last
        self.age=age
        User.active_users+=1

    def logout(self):
        User.active_users -=1
        return f'{self.first} has logged out'

    def full_name(self):
        return f'{self.first} {self.last}'  

    def initials(self):
        return f'{self.first[0]} {self.last[0]}'

    def likes(self,thing):
        return f'{self.first} likes {thing}'

    def is_senior(self):
        return self.age>=50

    def birthday(self):
        self.age+=1
        return f'Happy {self.age}th,{self.age}'                  


# user1=User('Robet','Peter',22)
# user2=User('William','Smith',51)

# print(user1.likes('Ice Cream'))
# print(user2.likes('fish and chilps'))

# print(user1.initials())
# print(user2.initials())

# print(user2.is_senior())
# print(user1.age)
# print(user1.birthday())
# print(user1.age)

print(User.active_users)
user1 = User("Joe", "Smith", 68)
user2 = User("Blanca", "Lopez", 41)
print(User.active_users)
print(user2.logout())
print(User.active_users)