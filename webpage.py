import streamlit as st
import pandas as pd
import numpy as np

import urllib.request
import sys

st.title('page title') # TODO
with open('apikey.txt', 'r') as file:   # get api key
    apikey = file.read().rstrip()

apilink1 = 'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/'
apilink2 = '?unitGroup=metric&elements=name%2Cdatetime%2Ctemp%2Cdew%2Chumidity%2Cwindspeed%2Ccloudcover%2Cvisibility%2Csolarenergy&include=days%2Cstats%2Cstatsfcst%2Cremote%2Cobs%2Cfcst&key=' + apikey + '&contentType=csv'

loc = st.text_input('Location')         # get location from user
loc = loc.replace(' ', '%20')

apilinkf = apilink1 + loc + apilink2    # concatenate link
if loc != '':
    try:         
        panda = pd.read_csv(urllib.request.urlopen(apilinkf))    # parse api return into pandas data format       
    except urllib.error.HTTPError  as e:                         # check for errors in url fetch
        ErrorInfo= e.read().decode() 
        st.write('Error code: ', e.code, ErrorInfo)
        sys.exit()
    except  urllib.error.URLError as e:
        ErrorInfo= e.read().decode() 
        st.write('Error code: ', e.code,ErrorInfo)
        sys.exit()

    st.write('Solar energy production data for ' + '**' + panda['name'][1]+ '**' + ':')     # write city name at top of page
    csvt = panda.loc[:,'datetime':]                                                         # TODO - remove later
    st.write(csvt)