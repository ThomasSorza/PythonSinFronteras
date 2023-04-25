# find the smallest number of a list

list = [45,-87,8,6,5,49,100,85]
smallest = 'init'

for x in list:
    if smallest == 'init':
        smallest = x
    elif (x < smallest):
        smallest = x

print(smallest)