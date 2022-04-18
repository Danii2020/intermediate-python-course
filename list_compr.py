# Lists Comprehensions
def increment_one_number(number):
    return 1 + number

def is_consonant(letter):
    vocals = 'aeiou'
    return letter.isalpha() and letter.lower() not in vocals

def run():
    paragraph = "Lleno de palabras"
    strange_tuple = (number for number in range(1, 101))
    filter_list = [letter for letter in paragraph if is_consonant(letter)]
    print(list(strange_tuple))

if __name__ == '__main__':
    run() 

