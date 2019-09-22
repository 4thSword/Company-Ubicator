#imports
import folium
from folium.plugins import HeatMap
from os import system

def print_map(subdf):
    values_coordinates = list(zip(subdf.latitude.values, subdf.longitude.values))
    heatmap = folium.Map([subdf.latitude.mean(), subdf.longitude.mean()], tiles='cartodbpositron', zoom_start=11)
    HeatMap(values_coordinates,radius= 45).add_to(heatmap)
    _ = system('mkdir ../output')
    heatmap.save('../output/map_ubication.html')
    _ = system('firefox ../output/map_ubication.html')