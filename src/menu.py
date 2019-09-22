#Menus descriptio
from display_menus import *
from data_processing import *
from map_representation import print_map
def main_menu(db):
    dev = get_developers_request(db)
    dev =clean_good_companies(dev)
    dev_cities = get_lisf_of_cities(dev)

    bad = get_bad_comapnies(db)
    bad = clean_bad_companies(bad)
    bad_cities = get_lisf_of_cities(bad)

    display_main_menu(dev_cities,bad_cities)
    input()

    recomended_cities = list(set(dev_cities).difference(set(bad_cities)))
    
    display_second_menu(recomended_cities)
    selected_city = input('Plese choose one of suggested cities:')
    
    companies = filter_df_by_city(dev,recomended_cities[int(selected_city)])
    print_map(companies)