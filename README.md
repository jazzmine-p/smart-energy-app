# Solar Wise Energy Forecast
A BostonHacks 2023 project by Grace Desroches, Sarah Cadet, Jasmine Pham, and Vijay Fisch

## Project Description
Solar Wise Energy Forecast is an machine learning powered algorithm that forecasts solar energy production based on up-to-date weather conditions.  Accurate green energy forecasting can help energy grid operators efficiently manage the integration of renewable energy sources, reduce reliance on fossil fuels, and minimize energy waste. The program could contribute to a more sustainable energy ecosystem and reduce greenhouse gas emissions. 

## Problem Formation
Renewable energy sources like solar panels are highly dependent on weather conditions, making their energy output variable and challenging to predict accurately. This variability can strain energy grids and affect the stability of power supply. We aim to optimize the integration of renewable energy into the grid. To accomplish this optimization, accurate forecasting is essential. 

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
1. Environmental Impacts
   - Green energy production is environmentally friendly. However, if we don’t maximize our use of green energy, we could be needlessly relying on fossil fuel when it is unnecessary. Accurate predictions allow us to improve the efficiency of green energy  by having better management of energy resources and reducing the need for backup fossil fuel plants.
   - Carbon Emission Reduction: By enabling users to forecast solar energy production, this project empowers individuals and organizations to reduce their reliance on traditional, fossil fuel-based energy sources. As a result, it directly contributes to carbon emission reduction efforts.
   - Climate Justice: By providing accurate solar energy forecasts, we empower Boston's diverse communities to make informed decisions about their energy consumption. This not only reduces their reliance on fossil fuels but also contributes to a more equitable and sustainable energy landscape.
   - Climate Resilience: The integration of GraphCast's advanced weather predictions, although currently beyond our technical scope, holds immense potential for early warnings of extreme weather events. This capability directly contributes to Boston's climate resilience efforts, safeguarding communities from the impacts of climate change.

2. Financial Impacts
   - Accurate predictions of green energy production enable grid operators to balance the supply and demand of electricity. This helps prevent blackouts and brownouts by ensuring that enough energy is available when needed. The prevention of blackouts and brownouts protects businesses from losing financial gains from either having to alter their hours of operation or losing server data.
    - Energy companies and investors need to make long-term decisions about infrastructure investments in renewable energy projects. Accurate predictions of green energy production help assess the viability and profitability of such projects.
    - Accurate predictions help energy providers avoid overcommitting or underutilizing resources. This can lead to cost savings by reducing the need for expensive peaker plants and minimizing energy wastage during periods of oversupply.

3. Technology Impacts
    - Technological Innovation: Our project represents a promising step towards harnessing emerging technologies, particularly AI, to combat climate change. We demonstrate a feasible concept, laying the groundwork for future technological advancements in the field of renewable energy integration.
      
4. Impact on Policies and Regulation
   - Governments and regulatory bodies use production forecasts to develop policies and regulations that promote the growth of renewable energy. Predictions provide essential data for setting renewable energy targets, incentivizing investments, and monitoring progress.

In summary, our project goes beyond technical innovation; it offers a tangible solution that addresses climate challenges, enhances climate justice, and fosters climate resilience. Our commitment to accurate solar energy forecasting, informed decision-making, and cutting-edge technology reflects our dedication to preparing Boston for the impacts of climate change and achieving a more sustainable future.
