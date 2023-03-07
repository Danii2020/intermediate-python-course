# Dictionary comprehensions

def dict_square_root(): # first exercise
    dict_of_numbers = {number:round(number ** (1/2), 3) for number in range(1, 11)}
    return dict_of_numbers

def dict_celcius(dict_of_tempsF): # second exercise   
    dict_of_tempsC = {key:round((val - 32)/1.8, 3) for (key, val) in dict_of_tempsF.items()}
    return dict_of_tempsC

def dict_even_odd(): # third exercise
    dict_of_numbers2 = {number:('even' if number % 2 == 0 else 'odd') for number in range(1, 11)}
    return dict_of_numbers2

def dict_with_lists(list1, list2): # fourth exercise
    # [claves, claves, claves]
    # [valores, valores, valores]
    # zip() => (clave, valor)
    dict_from_lists = {key:val for (key, val) in zip(list1, list2)}
    return dict_from_lists

def repeated_letter(text): # fifth exercise
    repeated_dict = {letter:text.count(letter) for letter in text.replace(" ", "")}    
    return repeated_dict

def run():
    text = "Estas letras se repiten"
    repeated_dict = repeated_letter(text)
    print(repeated_dict)

if __name__ == '__main__':
    run()