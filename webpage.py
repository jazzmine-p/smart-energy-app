import streamlit as st
import pandas as pd
import numpy as np

st.title('page title') # TODO

loc = st.text_input('Location')
st.write('The current location is', loc)

