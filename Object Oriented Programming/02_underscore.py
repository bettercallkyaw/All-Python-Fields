# _name
# __name
# __name__

class Person:
    # Init is a "dunder" method
    def __init__(self):
        self.name='bob smith'
        # single underscore means "private" (sort of)
        self._secret='hello'
        # two leading underscores tells Python to "mangle" the name
        self.__msg='i like noddle'
        self.__lol='nice to meet you'
        


person=Person()
print(person.name)
print(person._secret) #Anyone can still directly access the attribute
print(dir(person)) # Notice what __msg and __lol have been "mangled" to

print(person._Person__msg)
print(person._Person__lol)