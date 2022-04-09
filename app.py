from cProfile import label
import streamlit as st
from streamlit_folium import folium_static
import folium
import pandas as pd
import folium

#load and prepare the data.
csvpath = r'dataBase.csv'
df = pd.read_csv(csvpath)
df = df[['latitude','longitude','Name','desc','image','icon']]
df['desc'] = df['desc'].fillna('')

st.header('Melhores cidades para morar no Brasil')        
farmers_markets = folium.Map(location=[-20.4640173,-54.6162947],tiles = 'OpenStreetMap', zoom_start=4)
for index, row in df.iterrows():
        text = f"""
        <h4><b> {row.Name} </b></h4><br>  
        <p style="text-align:center;">
        <img src="{row.image}" alt="Farmer's Market Photo" style = "width:200px;height:200px;"> 
        
        <br>
        <p style="text-align:center;color:black">
        {row.desc}<br>
        </p>
            """
        #test = {row.icon}
        folium.Marker(
            [row['latitude'],row['longitude']],
            icon = folium.features.CustomIcon(row['icon'],icon_size=(40, 40)),
            popup = folium.Popup(text, max_width = 260, height= 260),
            tooltip = row['Name']).add_to(farmers_markets)
        

folium_static(farmers_markets, width=800, height= 450)