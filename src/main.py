#import libraries
from pymongo import MongoClient
from data_processing import *
import pandas as pd

#main function definition:
def main():
     db = database_connection()
     devreq = get_developers_request(db)
     print(devreq.head())

# start app exccuttion
if __name__ == "__main__":
   main()