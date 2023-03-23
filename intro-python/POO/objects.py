class User:
    """ name = "Thomas"
    lastName = "Shadex" """
    def __init__(self, name, lastName):
        self.name = name
        self.lastName = lastName
    
    #not necessary to have self but it's recommended
    def greeting(self):
        print('Hi, My name is ', self.name, self.lastName)

class Admin(User):
    def adminGreeting(self):
        print('Hi, My name is ', self.name, 'I am the admin.')

#here we create a user called user
user = User('Thomas', 'Sorza')


# print(user) #Memory direction
print(user.name, user.lastName)
user.greeting()
user.name = 'Arturo'
user.greeting()
""" del user.name
# user.greeting()
del user
print(user) """

admin = Admin('John','Ripper')
admin.greeting()
admin.adminGreeting()