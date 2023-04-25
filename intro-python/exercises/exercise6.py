#make a function to determine if a number is even or odd

def is_even(x):
    return x % 2 == 0

n = int(input('Enter a number: '))
print('The number is even: ' + str(is_even(n)))