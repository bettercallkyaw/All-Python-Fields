# A User class with 3 instance attributes but no instance methods(aside from,__init__)

class User:
    def __init__(self,first,last,age):
        self.first=first
        self.last=last
        self.age=age

    def full_name(self):
        return f'{self.first} {self.last}'

    def initials(self):
        return f'{self.first[0]} {self.last[0]}'

    def likes(self,thing):
        return f'{self.first} likes {thing}'

    def is_senior(self):
        return self.age>=65

    def birthday(self):
        self.age+=1
        return f'Happy {self.age}th, {self.first}'

user1=User('Robet','Peter',22)
user2=User('John','Mike',67)

print(user1.likes('ice scream'))
print(user2.likes('chicken'))

print(user1.initials())
print(user2.initials())

print(user2.is_senior())
print(user1.age) #Print age before we update it
print(user1.birthday()) #updates age
print(user1.age)#Print new value of age