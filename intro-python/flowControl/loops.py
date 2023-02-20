#loops
i = 0

#while
""" while i < 5:
    i += 1
    #i = i + 1
    if i == 3:
        continue #continue evaluation of condition
        #break breaks the loop
    print(i)
 """
#for Loop
""" users = ['thomas', 'felipe', 'Nicolas']

for user in users:
    print(user) """

""" user = 'THomas'

for c in user:
    print(c) """

""" users = ['thomas', 'felipe', 'Nicolas']

for user in users:
    if user == 'Nicolas':
        break
    print(user) """
""" 
users = ['thomas', 'felipe', 'Nicolas']

for user in users:
    if user == 'felipe':
        continue
    print(user) """
""" 
for x in range(3,30,3): #start range, finish range, addition
    print(x)
else: #finish of loop
    print('We have finished') """

#nested for
users = ['thomas', 'felipe', 'Nicolas']
ages = [24, 25, 26]

for user in users:
    for age in ages:
        print(user, age)