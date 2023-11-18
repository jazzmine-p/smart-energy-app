# [Project Name Here] 
A BostonHacks 2023 project by Grace, Sarah, Jasmine, and Vijay

## What problem are we trying to solve?
Renewable energy sources like solar and wind power are highly dependent on weather conditions, making their energy output variable and challenging to predict accurately. This variability can strain energy grids and affect the stability of power supply. We aim to optimize the integration of renewable energy into the grid. To accomplish this optimization, accurate forecasting is essential. 
## Our Approach
1. Data Collection
    - We gathered historical data on weather conditions and corresponding energy production data from solar energy farms
1. Data Processing & Features Engineering
    - We decided on the following relevant features from the weather data that can impact solar energy production:  cloud cover duration, visibility, dew point, humidity, windspeed, and solar energy.
1. Prediction of Weather & Solar Energy Production
    - We modeled a neural network that produces a [% of accuracy] accurate prediction of the solar energy production that is possible based on the imputed weather features.
    - For a larger accumulation of data, we would use Google’s AutoML model training and deployment tool VertexAI. We attempted to implement an AutoML model; however, the training dataset didn’t have a sufficient amount of rows.
1. Visualization and Reporting
    - We created a Streamlit app that allows users to input their location and receive a forecast of solar energy production for that day and the next 14 days. This app employs our prediction model and api calls to retrieve current and forecasted weather data and calculate a predicted solar energy production value.
## Impacts
What impacts can predicting solar energy production have?

