from modules.example1 import Animal


def instanciate_example():
    dog = Animal('Manchitas', 6)
    print(f"The name of this dog is {dog.name}, and its age is {dog.age} years old.\n")
    dog.eat('chicken')
    dog.walk()

def main():
    instanciate_example()

if __name__ == '__main__':
    main()