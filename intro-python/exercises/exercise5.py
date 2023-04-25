# check if the user is 18+
class User:
    def __init__(self, age):
        self.age = age

    def checkIsOnLegalAge(self):
        return self.age > 17

    def printAdvice(self):
        str = 'You are not on legal age'
        if self.checkIsOnLegalAge(): 
            str = 'You are on legal age! You can pass'
        print(str)

thomas = User(int(input('Enter your age: ')))
thomas.printAdvice()