import requests
import numpy as np
import pandas as pd
import dotenv 
import os
dotenv.load_dotenv()


meetup_token = os.getenv("MEETUP_KEY")

def getAuth(lon,lat):
    baseUrl = "https://api.meetup.com/find/upcoming_events?&key={}&sign=true&photo-host=public&lon={}&topic_category=design&page=500&radius=7&lat={}".format(meetup_token,lon,lat)
    print("Getting iformation from Meetups in the area... Please Wait")
    res = requests.get(baseUrl)
    response = res.json()
    return pd.DataFrame(response['events'])

def meetup_lat(venue):
    try:
        return venue.get('lat')
    except:
        return None
        
def meetup_lon(venue):
    try:
        return venue.get('lon')
    except:
        return None

def meetup_public(group):
    try:
        return group.get('who')
    except:
        return None

def meetup_cleaning(df):
    df['latitude']= df.venue.apply(meetup_lat)
    df['longitude']= df.venue.apply(meetup_lon)
    df['public']= df.group.apply(meetup_public)
    df = df[np.isfinite(df['longitude'])]
    return df