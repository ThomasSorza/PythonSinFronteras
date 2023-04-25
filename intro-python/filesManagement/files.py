c = open('./intro-python/filesManagement/file.txt', 'w')#the 1st parameter is the file name and the others are the permissions
#file name, read(r), append(a)/write(w), create(x)

#print(c.read())
c.write('Text written to file')

# print(c.read()) this reads all the file with .read()
# c.write('new line in our file')
c.close()

x = open('./intro-python/filesManagement/file.txt')
print(x.read())