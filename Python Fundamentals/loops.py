# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

people=['bob','jack','william','peter']

# Sample for loop
for person in people:
    print(f'current person=>{person}')

# break
for person in people:
    if person =='jack':
        break
    print(f'current break person=>{person}')

# continue
for person in people:
    if person =='jack':
        continue
    print(f'current continue person=>{person}')

# range
for i in range(len(people)):
    print(f'range person=>{people[i]}')

for i in range(1,10):
    print(f'number=>{i}')

# While loops execute a set of statements as long as a condition is true.
count =0
while count<=10:
    print(f'count number=>{count}')
    count+=1

############################################  
times=input('How many time do I have to tell you?')
times=int(times)

for time in range(times):
    print(f'time {time+1}:clean up your room')

############################################ 
for num in range(1,21):
    if num ==4 or num ==13:
        print(f"{num} is unlucky")
    elif num % 2==0:
        print(f"{num} is even")
    else:
        print(f"{num} is old")