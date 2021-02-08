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

a=4 #int
b=33.4 #float
fullName='Htin Kyaw' #str
isCool=False

print(fullName)

#mutiple assignment
x,y,city,isMarried=(3,4.5,'Boston',True)
print(isMarried)

#basic math
c=a+b 
print(c,type(c))

#casting
c=int(c)
print(c,type(c))
d=str(c)
print(d,type(d))

print('How many kilometers did you cycle today?')
kms=input()
miles=float(kms)/1.60934
miles=round(miles,2)
print(f'you {kms} km was ride {miles} miles')