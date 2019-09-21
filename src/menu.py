#Menus descriptio
from display_menus import *
from data_processing import *

def main_menu():
    dev = get_developers_request(db)
    dev =clean_good_companies(dev)
    dev_countries = 

    bad = get_bad_comapnies(db)
    bad = clean_bad_companies(bad)

    display_main():