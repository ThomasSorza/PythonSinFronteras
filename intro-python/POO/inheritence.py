class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound
    def greeting(self):
        print('Hello I am a ', self.type, ' and my name is ', self.name)

class Cat(Animal): #using super instance
    type = 'cat'
    def __init__(self, name, sound):
        super().__init__(name, sound)
        print('This is a extended Cat.')

class Dog(Animal): #using father class
    type = 'dog'
    def __init__(self, name, sound):
        Animal.__init__(self ,name, sound)
        print('This is a dog extended, using class Animal.')  

class Bird(Animal):
    type = 'bird'

cat = Cat('kitty', 'Meow')
cat.greeting()

dog = Dog('kaiser', 'bark')
dog.greeting()

bird = Bird('mordecai', 'OHHHh')
bird.greeting()