
from os import system

def clear():
    _ = system('clear')

def print_cities(lst):
    lista = ''''''
    for i in enumerate(lst):
         lista +='{}.- {}\n\n\t'.format(i[0],i[1])
    return lista

def display_main_menu(goodcities,badcities):
    clear()
    print('''
    ----------------------------------------------------------------------------------------------
    -  COMPANY UBICATOR                                                                          -
    ----------------------------------------------------------------------------------------------

    This App uses data from Crunchbase to find the perfect location for your Videogame Company!

    ----------------------------------------------------------------------------------------------

    Following the next criteria theese are the most significant cities to place your company:
    
    Criteria:

    1.- Tech companies that raises at least $1M.
    2.- Far from Videogames companies with at least 10 years.
    2.- With colse acces to Starbucks
    3.- Getting access to Design meetups
    ''')
    input("Press a key to show the cities list according your filters")
    clear()
    print('''
    ----------------------------------------------------------------------------------------------
    - The cities with more Tech companies that raised more than 1M dollar are :                  -
    ----------------------------------------------------------------------------------------------
        
        {}
    ----------------------------------------------------------------------------------------------
    - The cities with more VideoGames companies that have more than 10 years are :               -
    ----------------------------------------------------------------------------------------------

        {}
    
    '''.format(print_cities(goodcities),print_cities(badcities))
    )

