# SolarWise Energy Forecast
A BostonHacks 2023 project by Jasmine Pham, Grace Desroches, Sarah Cadet, and Vijay Fisch
[DevPost](https://devpost.com/software/solar-wise-energy-forecast)
[Energy Dashboard](https://app.powerbi.com/view?r=eyJrIjoiMjkxYzUxMmYtNGRmZi00MzI4LTgzNDItOGYzMWJhZjZkN2UzIiwidCI6ImQ1N2QzMmNjLWMxMjEtNDg4Zi1iMDdiLWRmZTcwNTY4MGM3MSIsImMiOjN9)
[Streamlit App](http://solarwise.biz/)

## Project Description
1. Problem: Renewable energy sources like solar panels are highly dependent on weather conditions, making their energy output variable and challenging to predict accurately. This variability can strain energy grids and affect the stability of power supply. Some challenges associated with solar energy prediction include:
    - Weather Forecasting Accuracy: Accurate solar energy predictions rely on precise weather forecasts. However, weather predictions, especially for longer time horizons, can have uncertainties. Small errors in weather forecasts can lead to significant discrepancies in solar energy production predictions.
    - Data Availability and Quality: Reliable historical weather data and solar energy production data are essential for training accurate prediction models. Data gaps or inaccuracies can lead to less reliable predictions.
    - Limited Forecasting Horizon: Weather forecasts typically provide predictions for a few days in advance. Accurate long-term predictions are more challenging to obtain, which can limit the ability to plan for future solar energy production accurately.
    - Grid Integration and Demand Fluctuations: Accurate predictions are crucial for grid operators to manage the integration of solar power into the electricity grid. Fluctuations in energy demand and supply must be balanced in real-time, which requires precise forecasts.
    - Geographic Variability: Solar energy potential varies significantly by geographic location. Accurate predictions require taking into account the specific conditions and solar resources of each region.

2. Solution: Solar Wise Energy Forecast is a machine learning powered algorithm that forecasts solar energy production based on up-to-date weather conditions.  Accurate green energy forecasting can help energy grid operators efficiently manage the integration of renewable energy sources, reduce reliance on fossil fuels, and minimize energy waste. The program could contribute to a more sustainable energy ecosystem and reduce greenhouse gas emissions. 

## Our Approach
1. Data Collection
    - We gathered historical data on weather conditions and corresponding energy production data from solar energy farms.
2. Data Processing & Features Engineering
    - We decided on the following relevant features from the weather data that can impact solar energy production:  cloud cover duration, visibility, dew point, humidity, windspeed, and solar energy.
3. Weather Forecast
    - We leveraged weather predictions obtained from a Visual Crossing's API, which supplies detailed weather forecasts for the upcoming 14 days.
    - Additionally, we explored the possibility of incorporating Google DeepMind's GraphCast, a state-of-the-art AI model just launched earlier this week that is capable of delivering exceptionally accurate 10-day weather predictions in under one minute. GraphCast offers advanced capabilities such as predicting the tracks of cyclones and identifying atmospheric rivers associated with flood risk, which could provide early warnings of extreme weather events. However, due to constraints in computing resources, we were unable to integrate GraphCast into our current model. This remains a promising avenue for future enhancements to our forecasting capabilities.
4. Prediction of Solar Energy Production
    - Armed with accurate weather forecasts, we leveraged machine learning models to predict solar energy production based on various weather conditions. Our model underwent rigorous testing with multiple algorithms, including Linear Regression, Long-Short Term Memory, and AdaBoosting.
    - Remarkably, our AdaBoosting model achieved an impressive R-squared value of 96%, providing a reliable prediction of solar energy production, essential for informed energy management in Boston.
    - For scalability, we plan to transition to Google Cloud's AutoML model training and deployment tool, VertexAI, as our dataset grows. Despite initial attempts, we encountered limitations due to the dataset's size.
5. Visualization and Reporting
    - To make our predictions accessible to users, we developed a user-friendly Streamlit application.
    - This application allows users to input their location (address, city, zipcode, etc.) and receive a 14-day forecast of solar energy production. The prediction comes from the Visual Crossing API.
    - Utilizing our prediction model and API calls, we retrieve real-time and forecasted weather data and calculate the anticipated solar energy production.
    - Furthermore, our application calculates the potential carbon emission reductions and cost savings achieved by transitioning to solar energy, bringing the climate benefits of renewable energy adoption closer to home.
      
## Impacts
What impacts can predicting solar energy production have?
1. Environment & Sustainability
   - Green energy production is environmentally friendly. However, if we don’t maximize our use of green energy, we could be needlessly relying on fossil fuel when it is unnecessary. Accurate predictions allow us to improve the efficiency of green energy  by having better management of energy resources and reducing the need for backup fossil fuel plants.
   - Carbon Emission Reduction: By enabling users to forecast solar energy production, this project empowers individuals and organizations to reduce their reliance on traditional, fossil fuel-based energy sources. As a result, it directly contributes to carbon emission reduction efforts.
   - Climate Justice: By providing accurate solar energy forecasts, we empower Boston's diverse communities to make informed decisions about their energy consumption. This not only reduces their reliance on fossil fuels but also contributes to a more equitable and sustainable energy landscape.
   - Climate Resilience: The integration of GraphCast's advanced weather predictions, although currently beyond our technical scope, holds immense potential for early warnings of extreme weather events. This capability directly contributes to Boston's climate resilience efforts, safeguarding communities from the impacts of climate change.

2. Resource Planning
     - Resource planning: Green energy sources like solar and wind are intermittent, meaning their energy production fluctuates based on weather conditions and time of day. Predicting their output helps grid operators and energy providers plan for periods of high and low energy production to ensure a stable and reliable energy supply.
     - Grid stability: Accurate predictions of green energy production enable grid operators to balance the supply and demand of electricity. This helps prevent blackouts and brownouts by ensuring that enough energy is available when needed.
     - Integration of renewables: As the share of renewable energy sources in the energy mix grows, it becomes crucial to integrate them efficiently into the existing energy infrastructure. Predictions of green energy production allow for better coordination with traditional power sources, reducing the need for backup fossil fuel generation and optimizing grid operations.

3. Financial Saving
    - Energy companies and investors need to make long-term decisions about infrastructure investments in renewable energy projects. Accurate predictions of green energy production help assess the viability and profitability of such projects.
    - Accurate predictions help energy providers avoid overcommitting or underutilizing resources. This can lead to cost savings by reducing the need for expensive peaker plants and minimizing energy wastage during periods of oversupply.

4. Policies and Regulation
   - Governments and regulatory bodies use production forecasts to develop policies and regulations that promote the growth of renewable energy. Predictions provide essential data for setting renewable energy targets, incentivizing investments, and monitoring progress.
  

In summary, our project goes beyond technical innovation; it offers a tangible solution that addresses climate challenges, enhances climate justice, and fosters climate resilience. Our commitment to accurate solar energy forecasting, informed decision-making, and cutting-edge technology reflects our dedication to preparing Boston for the impacts of climate change and achieving a more sustainable future.
