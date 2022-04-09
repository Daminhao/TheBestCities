from cProfile import label
import streamlit as st
from streamlit_folium import folium_static
import folium
import pandas as pd
import folium

#load and prepare the data.
csvpath = r'listcitys.csv'
df = pd.read_csv(csvpath)
df = df[['Latitude','Longitude','City','Desc','Image','Icon']]
df['Desc'] = df['Desc'].fillna('')

st.header ("Melhores cidades para morar no Brasil")
st.write('Fonte : [Embracon](https://www.embracon.com.br/blog/melhores-cidades-para-morar-no-brasil)')
        
farmers_markets = folium.Map(location=[-20.4640173,-54.6162947],tiles = 'OpenStreetMap', zoom_start=4)
for index, row in df.iterrows():
        
        text = f"""
        <h4><b> {row.City} </b></h4><br>  
        <p style="text-align:center;">
        <img src="{row.Image}" alt="Farmer's Market Photo" style = "width:200px;height:200px;"> 
        
        <br>
        <p style="text-align:center;color:black">
        {row.Desc}<br>
        </p>
            """
        folium.Marker(
            [row['Latitude'],row['Longitude']],
            icon = folium.features.CustomIcon(row['Icon'],icon_size=(40, 40)),
            popup = folium.Popup(text, max_width = 260, height= 260),
            tooltip = row['City']).add_to(farmers_markets)
        

folium_static(farmers_markets, width=800, height= 450)


### fonte

photo, info = st.columns([1, 1])

with photo:
    st.image('authorimg.png')

with info:
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.write('Danilo')
    st.write('Estudante de eng de Pesca pela UFMA(Universidade Federal do Maranhão)')
    st.write('Linkedin : [Danilo pereira](https://www.linkedin.com/in/danilo-oliveira-36a6208b/)')
    st.write('Twitter: https://twitter.com/danilologic')
