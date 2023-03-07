class Animal:
    # constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self, food):
        print(f"{self.name} is eating {food}.")

    def walk(self):
        print(f"{self.name} is walking.")


