c = open('file.txt')#the 1st parameter is the file name and the orthers are the permissions
#file name, read(r), append(a)/write(w), create(x)
for x in c:
    print(x)
""" print(c.readline()) """
# print(c.read()) this reads all the file with .read()

c.close()
