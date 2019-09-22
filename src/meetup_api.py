import requests
import dotenv 
import os
dotenv.load_dotenv()


meetup_token = os.getenv("MEETUP_KEY")

def getAuth(lon,lat, headers={"KEY={}=True".format(meetup_token)}):
    baseUrl = "https://api.meetup.com/find/upcoming_events?&sign=true&photo-host=public&lon={}}&page=20&radius=10&lat={}}".format(lon,lat)
    print("Asking {}".format(baseUrl))
    res = requests.get(baseUrl, headers=headers)
    return res.json()