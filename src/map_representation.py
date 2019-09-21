#imports
import folium
from folium.plugins import HeatMap

def print_map(subdf):
    values_coordinates = list(zip(subdf.latitude.values, subdf.longitude.values))
    heatmap = folium.Map([subdf.latitude.mean(), subdf.longitude.mean()], tiles='cartodbpositron', zoom_start=10)
    HeatMap(values_coordinates).add_to(heatmap)
    heatmap.save('../output/map_ubication.html')