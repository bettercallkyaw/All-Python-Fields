# Python has functions for creating, reading, updating, and deleting files.

# Open a file
myFile=open('index.txt','w')

#Get some info
print('name ',myFile.name)
print('is closed? ',myFile.closed)
print('mode ',myFile.mode)

# Write to file
myFile.write('hello i love ')
myFile.write('programming.')
myFile.close()

# Append to file
myFile=open('index.txt','a')
myFile.write('.i also love frameworks.')
myFile.close()

# Read to file
myFile=open('index.txt','r+')
text=myFile.read(200)
print(text)