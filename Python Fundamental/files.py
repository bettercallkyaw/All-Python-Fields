# Python has functions for creating, reading, updating, and deleting files.

# Open a file
myFile=open('index.txt','w')

#Get some info
print('Name ',myFile.name)
print('Is closed ',myFile.closed)
print('mode ',myFile.mode)

# Write to file
myFile.write('Hello I love')
myFile.write(' programming')
myFile.close()

# Append to file
myFile=open('index.txt','a')
myFile.write(' and computer hacking')
myFile.close()

# Read to file
myFile=open('index.txt','r+')
text=myFile.read(200)
print(text)