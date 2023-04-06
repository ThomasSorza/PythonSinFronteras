class Cat:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def greeting(self):
        print('Hello I am a cat and my sound is: ', self.sound)

cat = Cat('kitty', 'Meow')
cat.greeting()
