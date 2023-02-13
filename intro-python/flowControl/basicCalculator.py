print('welcome to your calculator!')
try:
    value1 = int(input('Type a number: '))    
except:
    value1 = 's'

if value1 == 's':
    print('Invalid input value')
    exit()

try:
    value2 = int(input('Type a second number: '))
except:
    value2 = 's'

if value2 == 's':
    print('Invalid input value')
    exit()

op = input('Type an option: ' + 
'\n' + '+: sum.' + 
'\n' + '-: less.' +
'\n' + '*: multiplication.' +
'\n' + '/: division.' + '\n')

if op == '+':
    print('The result value is: ' + str(value1 + value2))
elif op == '-':
    print('The result value is:' + str(value1 - value2))
elif op == '*':
    print('The result value is:' + str(value1 * value2))
elif op == '/':
    print('The result value is:' + str(value1 / value2))
else:
    print('Please type a valid option')