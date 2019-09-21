#import libraries
from data_processing import database_connection
from menu import main_menu

#main function definition:
def main():
     db = database_connection()
     main_menu(db)


# start app exccuttion
if __name__ == "__main__":
   main()