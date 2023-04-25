#get the volume of a sphere with the given radius
#formula: 4/3 pi * r^3
import math

radius = int(input('Please, enter the radius of the sphere: '))

def getVolumeSphere(r): #using python's math module
    return round(4/3 * math.pi * r ** 3, 2) #float value

print('The volume of the sphere is: ' + str(getVolumeSphere(radius)) + ' cubic units.')