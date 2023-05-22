class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def sit(self):
        print(self.name.title(),' can sit.')

    def roll(self):
        print('As ',self.name.title(),' at ',self.age,' can roll.')

class Puppy(Dog):
    def __init__(self,name,age):
        super().__init__(name,age)

    def dip(self):
        print(self.name,' is just a puppy!')






