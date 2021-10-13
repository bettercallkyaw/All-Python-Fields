# A function is a block of code which only runs when it is called. In Python, we do not use curly brackets, we use indentation with tabs or spaces

# Create function
def sayHello(name):
    print(f'hello {name}')

sayHello('bob smith')

# Return values
def getTotal(num1,num2):
    total=num1+num2
    return total

print(getTotal(4,4))

# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression. Very similar to JS arrow functions

def getResult(num3,num4):
    return num3+num4

print(getResult(5,5))

getValue=lambda num5,num6:num5+num6
print(getValue(6,6))
