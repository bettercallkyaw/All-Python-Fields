# If/ Else conditions are used to decide to do something based on something being true or false

x=20
y=10

# Comparison Operators (==, !=, >, <, >=, <=) - Used to compare values

# Simple if
if x>y:
    print(f'{x} values is greater than {y} values')

# if/Esle 
if x>y:
    print(f'{x} values is greater than {y} values')
else:
    print(f'{y} values is greater than {x} values')        

# elif
if x>y:
    print(f'{x} values is greater than {y} values')
elif (x==y):
    print(f'{x} values is equal to {y} values')    
else:
    print(f'{y} values is greater than {x} values')                

# Nested if
if x>5:
   if x<=20:
        print(f'{x} values is greater than 5 and less than or equal to 20')

# Logical operators (and, or, not) - Used to combine conditional statements

# and
if x>5 and x<=20:
  print(f'{x} values is greater than 5 and less than or equal to 20')

# or
if x>5 or x<=20:
  print(f'{x} values is greater than 5 and less than or equal to 20')

# if not
if not (x==y):
    print(f'{x} values is not equal to {y} values')

# Membership Operators (in, not in) - Membership operators are used to test if a sequence is presented in an object

members=[1,2,3,4,5,6,7,20]

# in
if x in members:
    print(x in members)

# not in
if y not in members:
    print(y not in members)

# Identity Operators (is, is not) - Compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:

# is
if x is y:
    print(x is y)

# is not
if x is not y:
    print(x is not y)

#############################################

# # ask for age
# age=input('How old are you?')

# if age:
#     age=int(age)
#     if age>=18 and age<21:
#         #18-21 writband
#         print('you can enter,but you need a wirtband')
#     elif age>=21:
#         #21+ drink,normal entery
#         print('you are good to entry and can drink')
#     else:
#         print('you can not enter!litter One!')
# else:
#     print('Please enter age!')

##################################################
print("Rock...")
print("Paper....")
print('Scissors...')

player1=input("Player 1,make your move:")
player2=input("Player2 ,make your move:")

# if player1 =="rock" and player2 =="scissors":
#     print("Player 1 wins")
# elif player1 =="rock" and player2 =="paper":
#     print("Player 2 wins")
# elif player1 =="paper" and player2 =="rock":
#     print("Player 1 wins")
# elif player1 =="paper" and player2 =="scissors":
#     print("Player 2 wins")
# elif player1 =="scissors" and player2 =="rock":
#     print("player 2 wins")
# elif player1 =="scissors" and player2=="paper":
#     print("player 1 wins")
# elif player1==player2:
#     print("It is a tie")  
# else:
#     print("something went wrong") 

if player1==player2:
    print("It is a tie")
elif player1=="rock":
    if player2=="scissors":
        print("player 1 wins")
    elif player2=="paper":
        print("Player 2 wins")
elif player1=="paper":
    if player2=="rock":
        print("player 1 wins")
    elif player2=="scissors":
        print("player 2 wins")
elif player1=="scissors":
    if player2=="paper":
        print("player 1 wins")
    elif player2=="rock":
        print("player 2 wins")
else:
    print("something went wrong")
