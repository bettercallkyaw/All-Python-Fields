# Core Modules
import datetime
from datetime import date

today=date.today()
#today=datetime.date.today()
print(today)

import time
from time import time

timestamps=time()
#timestamps=time.time()
print(timestamps)
# ------------------------
# -----------------------
##pip module
from camelcase import CamelCase

c=CamelCase()
print(c.hump("hello world"))

# -----------------------
##file module
import validator
from validator import validate_email

email="bob@gmail.com"

if validate_email(email):
    print("email is valid")
else:
    print("email is bad")    

#############################################################
from random import randint
x=randint(-100,100)
while x ==0: #  make sure x is not zero
    x=randint(-100,100)
y=randint(-100,100)
while y==0: # make sure y is not zero
    y=randint(-100,100)

if x>0 and y>0:
    print('both positive')
elif x<0 and y<0:
    print('both negative')
elif x>0 and y<0:
    print("x is positive and y is negative")
else:
    print('y is positive and y is negative')

###########################################################  
from random import choice,randint

actually_sick=choice([True,False])
kinda_sick=choice([True,False])
hate_your_job=choice([True,False])
sick_days=randint(0,10)

calling_in_sick=None 

if actually_sick and sick_days>0:
    calling_in_sick=True
elif kinda_sick and hate_your_job and sick_days>0:
    calling_in_sick=True
else:
    calling_in_sick=False