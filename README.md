# Stock Market Forecasting #
Team Members: Ami Kano (ak7ra), Theodore Thormann (nbx5kp), Royal Wang (rjw8ng)

## Motivation & Concrete Problem Statement:

The problem statement is as follows: What will the stock price be in the future for a set portfolio? Stock market prediction and analysis are some of the most difficult jobs to complete. There are numerous causes for this, including market volatility and a variety of other dependent and independent variables that influence the value of a certain stock in the market. These variables make it difficult for any stock market expert to anticipate the rise and fall of the market with precision. Machine learning algorithms are widely used by many organizations in stock market prediction. 

## Folder structure
* `ARIMA`: Test models for ARIMA
* `Data` : Data preprocessing notebook and datasets used in analysis
* `Final`: Final models with ARIMA, GRU, LSTM
* `GRU`: Test models for GRU
* `LSTM`: Test models for LSTM
* `daily_model_prediction.png`: Daily MSE bar graph
* `monthly_model_prediction.png`: Monthly MSE bar graph

## Experimental Design & Approach:

The experimental design will be split into three phases:
- Pre-Modeling Data Processing
  - Ensure quality of data through exploratory data analysis and data cleaning
      - Check for seasonality in data
  - Potentially reduce amount of columns used through feature selection
  - Split the data into a training and testing set
- Model Train and Testing
  - Time Series
    - Multivariate time-series model (ARIMA) forecasting the fluctuations in stock prices
    - Implemented using the Pandas and Statsmodels libraries
  - Long Short Term Memory (LSTM) and Gated Recurrent Unit (GRU)
    - Type of Recurrent Neural Network (RNN) used in time series predicting
    - Implemented using the Keras library in Python
- Model Performance Measurement
  - The performance of the time series model can be measured by the residual errors. We can also visualize the predictions made by the models and compare them to the true value.
  - The performance of the LSTM model can be measured using mean squared error. Similar to the Time Series model, we can visualize our predictions and compare them to the true value.


## DataSet:

Stock Market Data - Nifty 100 Stocks (1 min) data:
https://www.kaggle.com/datasets/debashis74017/stock-market-data-nifty-50-stocks-1-min-data
