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
1. Environmental Impacts
   - Green energy production is environmentally friendly. However, if we don’t maximize our use of green energy, we could be needlessly relying on fossil fuel when it is unnecessary. Accurate predictions allow us to improve the efficiency of green energy  by having better management of energy resources and reducing the need for backup fossil fuel plants.
2. Financial Impacts
   - Accurate predictions of green energy production enable grid operators to balance the supply and demand of electricity. This helps prevent blackouts and brownouts by ensuring that enough energy is available when needed. The prevention of blackouts and brownouts protects businesses from losing financial gains from either having to alter their hours of operation or losing server data.
    - Energy companies and investors need to make long-term decisions about infrastructure investments in renewable energy projects. Accurate predictions of green energy production help assess the viability and profitability of such projects.
    - Accurate predictions help energy providers avoid overcommitting or underutilizing resources. This can lead to cost savings by reducing the need for expensive peaker plants and minimizing energy wastage during periods of oversupply.
3. Impact on Policies and Regulation
   - Governments and regulatory bodies use production forecasts to develop policies and regulations that promote the growth of renewable energy. Predictions provide essential data for setting renewable energy targets, incentivizing investments, and monitoring progress.

