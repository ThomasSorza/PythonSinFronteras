class User:
    """ name = "Thomas"
    lastName = "Shadex" """
    def __init__(self, name, lastName):
        self.name = name
        self.lastName = lastName

#here we create a user called user
user = User('Thomas', 'Sorza')
user2 = User('Jean', 'Sorza')

# print(user) #Memory direction
print(user.name, user.lastName, user2.name, user2.lastName)