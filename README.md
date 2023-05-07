# Stock Market Forecasting #

## Project Overview

Stock price forecasting has been a popular research topic in the field of finance and economics. Accurately predicting the future value of a stock has significant implications for investors, traders, and financial analysts. In recent years, various machine learning and statistical methods have been applied to stock price forecasting. Among these methods, ARIMA, LSTM, and GRU have gained significant attention due to their ability to make accurate predictions and find dependencies using time series data.

This project presents a comparative study of ARIMA, LSTM, and GRU for stock price forecasting using a big data set over 60 GBs of Nifty 100 stock data tracked every minute from January 2015 to February 2022. The data set was further consolidated into showing monthly and daily prices to use as inputs into the models. The study uses the closing prices for a selected set of stocks from this data set and compares the forecasting performance of each model using mean squared error. The study also provides insights into the strengths and weaknesses of each model and discusses their potential applications in real-world scenarios.

## Problem Statement & Motivation:

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

## Data Pre-processing

The original 60 GB data set from Kaggle consists of time-series data from a portfolio of Nifty 100 stocks. Each stock contains 59 features detailing pricing values for every 5 minutes during a time period between February 2015 and October 2022.

This project used the University of Virginia's resource computing platform, Rivanna, which provided 2 TBs of memory allocation.

Downloading the dataset from Kaggle into Rivanna used python and Kaggle's API. First, a Kaggle API token was requested through a user's Kaggle profile. Once obtained, the opendatasets package was installed in Rivanna that helps download datasets from online sources such as Kaggle or Google Drive. Using the download function from this package, a zipped dataset was downloaded directly into a Rivanna folder. Once this zipped file was downloaded into the folder, the zipfile package was required to unzip the contents of the dataset containing the information on the 100 stocks. After unzipping the data file into Rivanna, 12 stocks were deleted because the stock contained less than 600,000 rows of data collected. Therefore, the time frame of the data did not match the remaining stocks. To provide more accurate predictions and assist with fitting the models, this data set was consolidated from the raw data. First, all the rows with overlapping time stamps were added together, forming one stock portfolio that consisted of all 88 stocks. This was done to increase the ability to run the multitude of models and focus on the machine learning aspect of the model's predictions. The resulting CSV file was approximately 707 MB and contained 639,981 rows. 

This new file was then used to create two data sets. One consolidates the file further into monthly stock closing prices and the second into daily stock closing prices. The reason for this split is to allow the models to provide more accurate predictions and to allow the training to complete within a reasonable time.
