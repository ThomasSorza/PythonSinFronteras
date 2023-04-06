class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound
    def greeting(self):
        print('Hello I am a ', self.type, ' and my name is ', self.name)

class Cat(Animal):
    type = 'cat'

class Dog(Animal):
    type = 'dog'    

class Bird(Animal):
    type = 'bird'

cat = Cat('kitty', 'Meow')
cat.greeting()

dog = Dog('kaiser', 'bark')
dog.greeting()

bird = Bird('mordecai', 'OHHHh')
bird.greeting()