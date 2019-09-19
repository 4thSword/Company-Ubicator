from pymongo import MongoClient
import pandas as pd
import re

def database_connection():
    # Creates a connection to our local database
    client = MongoClient("mongodb://localhost:27017/")
    return client.companies

def get_developers_request(db):
    # Returns a dataframe with all the companies that have "Tech" in tags
    regx = re.compile('\^?tech\w?',re.IGNORECASE)
    devreq = db.companies.find({"tag_list" : regx})
    return pd.DataFrame(devreq)

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