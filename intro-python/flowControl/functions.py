def myFunction():
    print('My first function')

#myFunction()

""" def printDatum(value): #argument
    print('Mi argument is', value)

printDatum('parameter 1') #parameter
 """
def printName(*names): # * allows to get multiple argument
    #print('The name is', name) #prints all arguments as a tuple
    for name in names:
        print('The name is',name)

#printName('Thomas', 'Sorza', 'Arturo') #parameter

def fullName(name, lastName):
    print(name, lastName)

#fullName(name = 'John', lastName = 'Suarez')

def fullName2(**kwargs): # **Kwargs stands for keyword arguments
    print(kwargs['name'], kwargs['lastName']) #accesing keys as a dictionary

#fullName2(name = 'John', lastName = 'Suarez')

def printDefault(name = 'thomas'): #if we define a name it will be executed as a default value
    print(name)

#printDefault('Arturo')
#printDefault()

def concatNames(names):
    allNames = ''
    for name in names:
        allNames += name + ' ' #concatenating names
    return allNames

# print('Your String of names is: ' + concatNames(['John', 'thomas', 'Juan']))

def myfunc(argument = 'this is an argument'):
    print(argument)

""" myfunc('thomas')
myfunc() """

def myfunc(list):
    for i in list:
        print(i)

# myfunc(['programming', 'Python'])

def contacNames(list):
    i=""
    for el in list:
        # i = i + ' ' + el;
        i += el;
    return i

print(concatNames(['Programming', 'Python']))