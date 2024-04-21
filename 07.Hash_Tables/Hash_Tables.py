class User:
    def __init__(self, name, age, magic):
        self.name = name
        self.age = age
        self.magic = magic

    def scream(self):
        print('aaaaaah!')

user = User(name='Kyle', age=54, magic=True)

print(user.name)  # Lookup O(1)
user.spell = 'abra kadabra'  # Insert O(1)
print(vars(user))
