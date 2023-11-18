import streamlit as st
import pandas as pd
import numpy as np

st.title('page title') # TODO
with open('apikey.txt', 'r') as file:
    apikey = file.read().rstrip()

apilink1 = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/"
apilink2 = "?unitGroup=metric&include=days&key=" + apikey + "&contentType=csv"

loc = st.text_input('Location')
loc = loc.replace(' ', '%20')

apilinkf = apilink1 + loc + apilink2
if loc != '':
    st.write(apilinkf)