# Import libraries
from pymongo import MongoClient
import pandas as pd
import re
import numpy as np

# Functios Definitions

def database_connection():
    # Creates a connection to our local database
    client = MongoClient("mongodb://localhost:27017/")
    return client.companies

def get_developers_request(db):
    # Returns a dataframe with all the companies that have "Tech" in tags
    regx = re.compile('\^?tech\w?',re.IGNORECASE)
    devreq = db.companies.find({"tag_list" : regx})
    return pd.DataFrame(devreq)

def get_bad_comapnies(db):
    # Returns a 
    bad = db.companies.find({'category_code': 'games_video' ,'founded_year': {'$lte':2009}})
    return pd.DataFrame(bad)

def expand_dataframe_by_offices(df):
    # Expand a dataframe to get one row per office.
    df = df.offices.apply(pd.Series) \
        .merge(df, right_index = True, left_index = True) \
        .drop(["offices"], axis = 1) \
        .melt(id_vars = ['_id', 'acquisition', 'acquisitions', 'alias_list', 'blog_feed_url',
           'blog_url', 'category_code', 'competitions', 'created_at',
           'crunchbase_url', 'deadpooled_day', 'deadpooled_month',
           'deadpooled_url', 'deadpooled_year', 'description', 'email_address',
           'external_links', 'founded_day', 'founded_month', 'founded_year',
           'funding_rounds', 'homepage_url', 'image', 'investments', 'ipo',
           'milestones', 'name', 'number_of_employees', 'overview',
           'partners', 'permalink', 'phone_number', 'products', 'providerships',
           'relationships', 'screenshots', 'tag_list', 'total_money_raised',
           'twitter_username', 'updated_at', 'video_embeds'], value_name = "offices") \
        .drop("variable", axis = 1)
    return df



def drop_nulloffices(df):
    df.dropna(subset= ['offices'])
    return df


def get_lat(x): 
    # Get latitude for a given office object
    try: 
        lat = x.get('latitude')
    except: 
        lat = None
    return lat

def get_lon(x): 
    # Get longitude for a given office object
    try: 
        lat = x.get('longitude')
    except: 
        lat = None
    return lat

def geopoint(office): 
    # Creates a geopoint object from an give office
    return {"type": "Point", "coordinates": [get_lon(office),get_lat(office)]}


def get_amouts_raised(funding_round):
    # creates a list of the values raised in every round for a company
    return [x.get('raised_amount') for x in funding_round]

def drop_Raised_nones(lst):
    for element in lst:
        if element == None:
            lst.remove(element)
    return lst

def create_total_raised(lst):
    try:
        return sum(lst)
    except:
        return 0

def get_city(office):
    try:
        return office['city']
    except:
        return None



def clean_good_companies(df):
    #get the data from Mongo db and start a first filtering:
    df = expand_dataframe_by_offices(df)
    df['raised'] = df.funding_rounds.apply(get_amouts_raised)
    df.raised.apply(drop_Raised_nones)
    df['total_raised'] = df.raised.apply(create_total_raised)
    df = df[df['total_raised']>= 900000]
    df = df[['name','category_code','total_raised','offices']]
    df = drop_nulloffices(df)
    df['City'] = df.offices.apply(get_city)
    df = df[df['City']!= ""]
    df['geo'] = df.offices.apply(geopoint)
    df['longitude'] = df.offices.apply(get_lon)
    df['latitude'] = df.offices.apply(get_lat)
    return df

def clean_bad_companies(df):
    #get the data from Mongo db and start a first filtering:
    df = expand_dataframe_by_offices(df)
    df = df[['name','offices']]
    df = drop_nulloffices(df)
    df['City'] = df.offices.apply(get_city)
    df = df[df['City']!= ""]
    df['geo'] = df.offices.apply(geopoint)
    df['longitude'] = df.offices.apply(get_lon)
    df['latitude'] = df.offices.apply(get_lat)
    return df

def get_lisf_of_cities(df):
    subdf = df.groupby(['City']).agg({'name':"count"}) 
    subdf = subdf.sort_values(by="name", ascending=False)
    return list(subdf.index)[:6] 


def filter_df_by_city(df,city):
    #given a city, filters our dataframe:
    subdf = df[df['City']== city]
    subdf = subdf[np.isfinite(subdf['longitude'])]
    return subdf