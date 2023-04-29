# necessary Python packages
import os
import pandas as pd
import time


# get list of csv's
os.chdir("/gpfs/gpfs0/project/SDS/instructional/ds5110_sp23_finalproject/stock-market-data-nifty-50-stocks-1-min-data/")
csv_list = os.listdir()
csv_list.remove('1. Data description.txt')
csv_list.remove('.ipynb_checkpoints')


# instantiate dataframe
aggregated_df = pd.read_csv(csv_list[0])
aggregated_df.date = pd.to_datetime(aggregated_df.date)
aggregated_df = aggregated_df.set_index("date")
aggregated_df = aggregated_df

# go through list of csv's
for i in range(1, len(csv_list)):
    
    start_time = time.time()
    
    df2 = pd.read_csv(csv_list[i])
    df2.date = pd.to_datetime(df2.date)
    df2 = df2.set_index("date")
    
    intersection = aggregated_df.index.intersection(df2.index)
    
    aggregated_df = aggregated_df.loc[intersection] + df2.loc[intersection]
    
    end_time = time.time()
    
    print(f"Finished {i+1} out of {len(csv_list)} files: {end_time - start_time:.2f} seconds")
    
      
# save dataframe to csv
os.chdir("/gpfs/gpfs0/project/SDS/instructional/ds5110_sp23_finalproject/")
aggregated_df.to_csv("aggregate_data.csv")