# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 09:37:50 2021

@author: rajauskas
"""

import geopandas
import geopy
import pandas as pd
import folium

from geopy.geocoders import Nominatim

locator = Nominatim(user_agent = "myGeolocator")
location = locator.geocode("Champ de Mars, Paris, France")

print("Latitude = {}, Longitude = {}".format(location.latitude, location.longitude))

amici = [
"Pumba",
"Renan",
"Vic",
"Flor",
"Ajx",
"Chico",
"Luiz",
"Gabriel"]

cidades = [
"Atibaia",
"Campinas",
"São Carlos",
"Nantes",
"Lisboa",
"Santa Isabel",
"São Paulo",
"Rio de Janeiro",
]


df = pd.DataFrame({'amico':amici,'cidade':cidades})
print(df)

df['gcode'] = df["cidade"].apply(locator.geocode)
df['lat'] = [g.latitude for g in df.gcode]
df['long'] = [g.longitude for g in df.gcode]
avglat = df['lat'].mean()
avglong = df['long'].mean()

m = folium.Map(location=[avglat, avglong], zoom_start=3, tiles="Stamen Terrain")

tooltip = "Aqui!"

folium.Marker(
    [avglat, avglong], popup="<i>Centro Geográfico de los amici</i>", tooltip=tooltip,icon=folium.Icon(color="green")
).add_to(m)


df = df[['amico','lat','long']]

for index, location_info in df.iterrows():
    folium.Marker([location_info["lat"], location_info["long"]], popup=location_info["amico"]).add_to(m)
    
m.save("Mapa.html")
