import streamlit as st
import pandas as pd
import numpy as np

import urllib.request
import sys

from sklearn.metrics import r2_score, mean_squared_error
from sklearn.ensemble import AdaBoostRegressor
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

st.title('page title') # TODO

forecast = []

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
    # st.write(forecast.loc[:, 'datetime':])
    return forecast

def graph():
    st.area_chart(forecast, x='datetime', y='solar output')

def predict(vs_test):
    d = {'solar output': []}
    
    vs_test['datetime'] = pd.to_datetime(vs_test['datetime'])
    vs_test['year'] = vs_test['datetime'].dt.year
    vs_test['month'] = vs_test['datetime'].dt.month
    vs_test = vs_test.drop(columns=['datetime', 'name'])

    final_ada = AdaBoostRegressor(base_estimator=None, 
                            learning_rate=0.5, 
                            n_estimators=150,
                            random_state=42)
    
    vs_pred = final_ada.predict(vs_test)
    st.write(vs_pred)
    
    d['solar output'] += [2]
    d['solar output'] += [3]
    d['solar output'] += [4]
    vs_test = vs_test.join(pd.DataFrame(data=d))
    # st.write(vs_test.loc[:, ['datetime', 'temp', 'cloudcover', 'visibility', 'solar output']], use_container_width=True)

    return vs_test
  

loc = st.text_input('Location')         # get location from user
if loc != '':
    link = gen_link(loc)
    forecast = gen_data(link)
    forecast = predict(forecast)
    graph()