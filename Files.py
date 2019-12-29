myFile = open('myfile.txt', 'w')
print('Name: ', myFile.name)
print('Is Closed: ', myFile.closed)
print('opening Mode: ', myFile.mode)

myFile.write('I love Python')
myFile.close()

myFile = open('myFile.txt','a')
myFile.write(' I also like PHP')
myFile.close()

myFile = open('myfile.txt', 'r+')
text = myFile.read(10)
print(text)