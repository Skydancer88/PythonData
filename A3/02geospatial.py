# Do the relevant imports of pandas and folium
import pandas as pd
import folium 
import os

# Import requests, zipfile, io to unpack our zipped data
import requests, zipfile, io

# get data from web is does not exist locally
if os.path.isfile('2021 Census GCP States and Territories for AUS/2021Census_G01_AUST_STE.csv') == False:
    datapack_2021_zipped = requests.get('https://www.abs.gov.au/census/find-census-data/datapacks/download/2021_GCP_STE_for_AUS_short-header.zip')
    datapack_2021 = zipfile.ZipFile(io.BytesIO(datapack_2021_zipped.content))
    datapack_2021.extractall()

# read in data
census_data = pd.read_csv('./2021 Census GCP States and Territories for AUS/2021Census_G01_AUST_STE.csv')
australian_states = requests.get('https://raw.githubusercontent.com/tonywr71/GeoJson-Data/master/australian-states.json').json()

# This code produces the vis shown at the top of this question
m_australia = folium.Map(location=(-23.07, 132.08), zoom_start=5)

folium.Choropleth(
    geo_data=australian_states,
    data=census_data,
    columns=["STE_CODE_2021", "Tot_P_P"],
    key_on='feature.id',
    fill_color='RdBu'
).add_to(m_australia)

m_australia.save('02.html')
