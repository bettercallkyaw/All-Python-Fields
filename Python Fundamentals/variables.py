# A variable is a container for a value, which can be of various types

'''
This is a 
multiline comment
or docstring (used to define a functions purpose)
can be single or double quotes
'''

"""
VARIABLE RULES:
  - Variable names are case sensitive (name and NAME are different variables)
  - Must start with a letter or an underscore
  - Can have numbers but can not start with one
"""

a=5 # int
b=5.5 # float
name="bob" # string
isMarried=False # bool

print(name)

#mutiple assignment
(x,y,city,isCool)=(3,4.5,"boston",True)
print(city)

#basic math
c=a+b 
print(type(c),c)

#casting
c=int(c)
print(type(c),c)
d=str(c)
print(type(d),d)

print('How many kilometers did you cycle today?')
kms=input()
miles=float(kms)/1.60934
miles=round(miles,2)
print(f'you {kms} km was ride {miles} miles')