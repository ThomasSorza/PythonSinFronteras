#This is a comment

#canditionals

if 3 > 5:#This is a comment
    print('Esto no se va a imprimir')

#if 5 > 3:#This is other comment
 #   print('5 es mayor a 3')

x = 5
y = 'chachito feliz'

#primitiveTypes

#print(x, y)

email = 'thomas@correo.com'
#print(email)

#Can't start with number
_mi_var = 'chanchito'
_miVar = 'chanchitos'
MIVAR = 'CHANCHITo'
a,b,c = 'lala', 'lele', 'lili'
#print(a, b, c)

valor1 = valor2 = valor3 = 'canchito_feliz'
#print(valor1, valor2, valor3)

#Concat
inicio = 'Hola '
final = 'mundo'
#print(inicio + final)

#Is diferent that use the , (the coma adds a space)
#inicio = 'Hola '
#final = 'mundo'
#print(inicio, final)

palabra = 'hola mundo' #String
oracion = "hola mundo comilla doble" #String

entero = 20 #integer
conDecimales = 20.2 #float
complejo = 1j #complejos

#print(palabra, oracion, entero, conDecimales, complejo)

#Lists

lista = ['hola','mundo','chanchito feliz']
Array1 = [4,4,5]
lista2 = lista.copy()
lista2.append(4)
lista.append(5)
#lista.clear()
#print(lista, lista2.count(2), Array1.count(4))
#print(len(lista), len(lista2))
largolista = len(lista) 
largolista2 = len(lista2)

#print(largolista, largolista2)

#print(lista[2])

#lista2.pop() #removes last element
# lista2.pop()
#lista2.remove('hola') #remove specific item
#print(lista2)
lista.pop()
lista.sort() #must be all elements of the same type
# print(lista)
lista.reverse()
# print(lista)

#tuples 

tuple = ('hi', 'this', "is", 'a', 'tuple')
#print(tuple)
# tuple.append('hola')
listaTuple = list(tuple)
# print(listaTuple)
listaTuple.append('yes')
# print(listaTuple)

# rages

range = range(8)
#print(range)

#dictionaries

dictionary = {
    "name": "max",
    "race": "persa",
    "age" : 3
}
""" 
print(dictionary)
print(dictionary["name"])
print(dictionary.get("race")) """
dictionary["age"] = 14
""" print(dictionary)
print(len(dictionary)) """
#catCopy = dictionary.copy()
catCopy = dict(dictionary)
dictionary['purrs'] = 'yeah'
# print(dictionary)
dictionary.pop("name")
# print(dictionary)
#dict.popitem()
#print(dictionary)
#del dict["purrs"]
dictionary.clear()
#print(dictionary, catCopy)

#Dictionary of dictionaries
""" kitties = {
    "Cat1" :{
         "name":"Fliffy",
        "age" : 5
    },
    "Cat2" :{
        "name":"Kenneth",
        "age" : "2",
    }
} """

#another way to declare it
fliffy = {
    "name":"Fliffy",
    "age" : 5
}
kenneth = {
    "name":"Kenneth",
    "age" : "2",
}
kitties = {
    "cat1" : fliffy,
    "cat2" : kenneth
}
# print(kitties)
#dict Constructor
human = dict(name="thomas", age="20")
# print(human)

#boolean
booleanV = True
#boolean2 = false
boolean2 = False
# print(booleanV, boolean2)