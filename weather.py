import requests


def main():
    '''
    This function takes a city and return 
    the weather of that city.
    '''
    city = input("Give a city: ")
    url = f'https://wttr.in/{city}'
    weather = requests.get(url).text
    print(weather)



if __name__ == '__main__':
    main()