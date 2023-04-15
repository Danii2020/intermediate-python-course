from animal import Animal


class Dog(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def give_love(self):
        print(f"{self.name} is giving love!")

    def sleep(self):
        print('I sleep 5 hours!')


class GermanShepherd(Dog):
    def __init__(self, name, age, color):
        super().__init__(name, age, color)

class Cat(Animal):
    def __init__(self, name, age, lives):
        super().__init__(name, age)
        self.lives = lives

    def do_parkour(self):
        print(f"{self.name} is doing parkour!")

    def sleep(self):
        print('I sleep 20 hours!')


dog = Dog('Manchitas', 6, 'white')
cat = Cat('Garfield', 10, 3)
german_shepherd = GermanShepherd('Antion', 4, 'brown')

print('Dog:')
dog.sleep()
dog.give_love()
german_shepherd.give_love()
print('Cat:')
cat.sleep()
cat.do_parkour()
# print(f"This dog is {dog1.name}, is {dog1.age} years old, and its color is {dog1.color}")

