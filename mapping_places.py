import folium
import pandas as pd
from geopy.geocoders import ArcGIS

nom = ArcGIS()
df = pd.read_csv('places.csv')

def map_creator(df):
    lats = df['Latitude']
    longs = df['Longitude']
    memory = df['Memory']
    lived = df['Lived']
    map = folium.Map(location = [0, -0], zoom_start = 2.4, tiles = 'Stamen Terrain')

    for lat_,long_, _memory, _lived in zip(lats, longs, memory, lived):
        if _lived == 1:
            map.add_child(folium.Marker(location = [lat_,long_], popup = _memory, icon = folium.Icon(icon = 'circle', color = 'lightgreen')))
        else:
            map.add_child(folium.Marker(location = [lat_,long_], popup = _memory, icon = folium.Icon(icon = 'circle', color = 'orange')))
            
        map.save('map_places.html')
    return 'map_places.html'

def geolocation(df):
    df['Coordinates'] = df['Location'].apply(nom.geocode)
    df['Latitude'] = df['Coordinates'].apply(lambda x: x.latitude if x != None else None)
    df['Longitude'] = df['Coordinates'].apply(lambda x: x.longitude if x != None else None)
    df.drop(['Coordinates'], axis  = 1)
    return df

geolocation(df)     
map_creator(df)