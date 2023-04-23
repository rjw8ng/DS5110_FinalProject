import os
import pandas as pd
import numpy as np
from datetime import datetime
from statsmodels.tsa.arima.model import ARIMA
import statsmodels.api as sm
#from statsmodels.graphics.tsaplots import plot_predict
import matplotlib.pyplot as plt
#from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
#from statsmodels.tsa.seasonal import seasonal_decompose
from sklearn.metrics import mean_squared_error
from math import sqrt
from matplotlib import pyplot
from statsmodels.tsa.stattools import adfuller
from pmdarima import auto_arima
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
from pmdarima.arima import auto_arima
import time
import warnings
warnings.filterwarnings('ignore')
from tqdm.notebook import tqdm

#--------------------------------------------------------------------------------

data_dir = "/gpfs/gpfs0/project/SDS/instructional/ds5110_sp23_finalproject/"

agg_data_monthly = pd.read_csv(data_dir + "aggregate_data_daily.csv", parse_dates=True)
agg_data_monthly['date'] = pd.to_datetime(agg_data_monthly.date).dt.strftime("%Y-%m")
agg_data_monthly.sort_values(by='date',ascending=False)
agg_data_monthly = agg_data_monthly.groupby(["date"]).mean()
agg_data_monthly.index = pd.DatetimeIndex(agg_data_monthly.index)

train_len_monthly = int(len(agg_data_monthly)*0.8)
train_monthly = agg_data_monthly.close[:train_len_monthly]
test_monthly = agg_data_monthly.close[train_len_monthly:]
train_monthly.index = pd.DatetimeIndex(train_monthly.index).to_period('M')
test_monthly.index = pd.DatetimeIndex(test_monthly.index).to_period('M')

#--------------------------------------------------------------------------------

result = pd.DataFrame({'Order' : [], 'MSE' : []})

orders_list = []

for p in range(4):
    for d in range(3):
        for q in range(12):
            orders_list.append((p, d, q))
            for x in range(5, 13, 1):
                orders_list.append((p, d, q, x))

counter = 0

for order in tqdm(orders_list):
    
    try:
        if len(order)==3:
            model_monthly = ARIMA(train_monthly, order=order) 
        else:
            model_monthly = ARIMA(train_monthly, seasonal_order=order)
            
        model_monthly = model_monthly.fit()
        pred_monthly = model_monthly.predict(start=train_len_monthly, end = len(agg_data_monthly)-1, typ='levels')
        mse_monthly = mean_squared_error(test_monthly, pred_monthly)
        
        temp = pd.DataFrame({'Order' : [order], 'MSE' : [mse_monthly]})
        result = pd.concat([result,temp])
        
    except:
        temp = pd.DataFrame({'Order' : [order], 'MSE' : [np.nan]})
        result = pd.concat([result,temp])
    
    counter += 1
    if counter % 100 == 0:
        print("Current best:", result.sort_values('MSE', na_position='last').head(1).Order[0],
             "at MSE of", result.sort_values('MSE', na_position='last').head(1).MSE[0])
        result.sort_values('MSE', na_position='last').to_csv(data_dir+"arima/order_mse.csv")