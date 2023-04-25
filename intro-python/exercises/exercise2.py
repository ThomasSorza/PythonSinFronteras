#enter name and lastName and print it backwards.

name = input("Enter name: ")
lastName = input("Enter last: ")
fullName = name + ' ' + lastName

print(fullName[::-1]) # ::-1 slice to reverse string

backward = ''

#second way to solve the problem:
for i in range(len(fullName) -1, -1, -1):
    backward += fullName[i]

print(backward)