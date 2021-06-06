# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 18:41:55 2021

@author: tapan
"""


import pandas as pd
import glob
import time
 
def calculate_aqi_2013_2018():
    files = glob.glob('Data/AQI/' + '*.csv')
    aqi_2013_2018 = []
    for file in files:
        for day in pd.read_csv(file,chunksize=24):
            day_aqi_total = 0
            day_aqi_avg = 0
            data = []
            df = pd.DataFrame(data = day)
            for index,rows in df.iterrows():
                data.append(rows['PM2.5'])
            for i in data:
                if type(i) is int or type(i) is float:
                    day_aqi_total = day_aqi_total + i
                elif type(i) is str:
                    if i == 'NoData'  or i == 'PwrFail' or i == '---' or i == 'InVld':
                        continue
                    else:
                        day_aqi_total = day_aqi_total + float(i)
            day_aqi_avg = day_aqi_total/24
            aqi_2013_2018.append(day_aqi_avg)
    return aqi_2013_2018
if __name__ == "__main__":
    start_time = time.time()
    aqi_list = calculate_aqi_2013_2018()
    end_time = time.time()
    print("total time for data collection {}".format(end_time-start_time))
        
    

                     