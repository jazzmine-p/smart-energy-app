import streamlit as st
import pandas as pd
import numpy as np

import urllib.request
import sys

import pandas as pd
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.ensemble import AdaBoostRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.ensemble import AdaBoostRegressor
from sklearn.tree import DecisionTreeRegressor

import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

st.set_page_config(page_title='SolarWise', page_icon='Solar Wise Logo.png', layout='wide')
col1, col2 = st.columns([0.1, 0.9], gap="small")
col1.image('Solar Wise Logo.png', use_column_width=True)
col2.title('SolarWise Energy Forecast')
col2.markdown('Enter your location for a 15 day solar panel production forecast')
# primary color = #427F13

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
    col2.area_chart(forecast, x='Date', y='Predicted Solar Output (kW/hr)', color=(66, 127, 19, 150))

def predict(vs_test):
    df = pd.read_csv("joined-weather-solar.csv")
    #df['Date'] = pd.to_datetime(df['Date'])
    #df['year'] = df['Date'].dt.year
    #df['month'] = df['Date'].dt.month
    #df['day'] = df['Date'].dt.month
    df = df.drop(columns=['Date','Station pressure', 'Unnamed: 0', 'Altimeter'])
    df = df.rename(columns={'Temperature':'temp',
                            'Dew point':'dew',
                            'Wind speed':'windspeed',
                            'Cloud coverage': 'cloudcover',
                            'Visibility': 'visibility',
                            'Solar energy': 'solarenergy',
                            'Relative humidity':'humidity'})
    X = df.drop(columns=['Site Performance Estimate'], axis=1)
    y = df['Site Performance Estimate']

    # Splitting the dfset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=37)

    # Normalizing the df
    # scaler = MinMaxScaler(feature_range=(0, 1))
    # X_train = scaler.fit_transform(X_train)
    #X_test = scaler.transform(X_test)

    vs_test_df = vs_test

    # Preprocess the data
    #vs_test['Date'] = pd.to_datetime(vs_test['datetime'])
    #vs_test['year'] = vs_test['Date'].dt.year
    #vs_test['month'] = vs_test['Date'].dt.month
    #vs_test['day'] = vs_test['Date'].dt.day
    vs_test = vs_test.drop(columns=['Date', 'name'])

    # Reorder column and MinMaxScaler
    vs_test = vs_test[['cloudcover', 'visibility', 'temp', 'dew', 'humidity', 'windspeed',
        'solarenergy', 'year', 'month', 'day']]
    # vs_test = scaler.transform(vs_test)

    # Predict using AdaBoosting based on DecisionTreeRegressor base tree
    base_tree = DecisionTreeRegressor(max_depth=3, random_state=37)
    base_tree.fit(X_train, y_train)
    
    final_ada = AdaBoostRegressor(base_estimator=base_tree, 
                                learning_rate=1, 
                                n_estimators=150,
                                random_state=37)
    result = final_ada.fit(X_train, y_train)

    # Final prediction
    vs_pred = result.predict(vs_test)

    vs_test_df = vs_test_df.join(pd.DataFrame(data=vs_pred, columns=['Predicted Solar Output (kW/hr)']))
    col1.dataframe(vs_test_df.loc[:, ['Date', 'Predicted Solar Output (kW/hr)']], use_container_width=True, hide_index=True)

    return vs_test_df
  

loc = st.text_input('Location')         # get location from user
if loc != '':
    link = gen_link(loc)
    forecast = gen_data(link)
    col1, col2 = st.columns([0.3, 0.7], gap="small")
    forecast = predict(forecast)
    graph()
