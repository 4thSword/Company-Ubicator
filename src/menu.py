#Menus descriptio
from display_menus import *
from data_processing import *

def main_menu(db):
    dev = get_developers_request(db)
    dev =clean_good_companies(dev)
    dev_countries = get_lisf_of_cities(dev)

    bad = get_bad_comapnies(db)
    bad = clean_bad_companies(bad)
    bad_countries = []#get_lisf_of_cities(bad)
    display_main_menu(dev_countries,bad_countries)