import streamlit as st
import pandas as pd
import numpy as np

import urllib.request
import sys

st.title('page title') # TODO
forecast = None

def gen_link(loc):
    with open('apikey.txt', 'r') as file:   # get api key
        apikey = file.read().rstrip()

    apilink1 = 'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/'
    apilink2 = '?unitGroup=metric&elements=name%2Cdatetime%2Ctemp%2Cdew%2Chumidity%2Cwindspeed%2Ccloudcover%2Cvisibility%2Csolarenergy&include=days%2Cstats%2Cstatsfcst%2Cremote%2Cobs%2Cfcst&key=' + apikey + '&contentType=csv'

    loc = loc.replace(' ', '%20')

    return apilink1 + loc + apilink2    # concatenate link

def gen_data(link):
    try:         
        forecast = pd.read_csv(urllib.request.urlopen(link))       # parse api return into forecasts data format       
    except urllib.error.HTTPError as e:                         # check for errors in url fetch
        ErrorInfo= e.read().decode() 
        st.write('Error code: ', e.code, ErrorInfo)
        sys.exit()
    except  urllib.error.URLError as e:
        ErrorInfo= e.read().decode() 
        st.write('Error code: ', e.code,ErrorInfo)
        sys.exit()

    st.write('Solar energy production data for ' + '**' + forecast['name'][1]+ '**' + ':')     # write city name at top of page
    st.write(forecast.loc[:,'datetime':])
    return forecast

def graph():
    st.area_chart(forecast, x='datetime', y='temp')

loc = st.text_input('Location')         # get location from user
if loc != '':
    link = gen_link(loc)
    forecast = gen_data(link)
    graph()