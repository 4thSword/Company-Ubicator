#imports
import folium
from folium.plugins import HeatMap
from os import system
from meetup_api import *

def print_map(subdf):
    lon = subdf.longitude.mean()
    lat = subdf.latitude.mean()
    values_coordinates = list(zip(subdf.latitude.values, subdf.longitude.values))
    heatmap = folium.Map([lat, lon], tiles='cartodbpositron', zoom_start=11)
    HeatMap(values_coordinates,radius= 45).add_to(heatmap)
    meetups = getAuth(lon,lat)
    meetups = meetup_cleaning(meetups)
    meetups_coordinates = list(zip(meetups.latitude.values, meetups.longitude.values))
    
    for tuple in meetups_coordinates:
        folium.Marker(tuple,radius =1,
                        icon=folium.Icon(icon='cloud'), # Icono nube, hay más en la documentación
                        fill_color="#F35C50",
                       ).add_to(heatmap)
    
        pass
    heatmap.save('../output/map_ubication.html')
    _ = system('firefox ../output/map_ubication.html')