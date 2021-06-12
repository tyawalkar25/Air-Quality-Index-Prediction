# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 19:32:07 2021

@author: tapan
"""

import glob
import pandas as pd
import os
from AQI_data_collection import calculate_aqi_2013_2018

def get_features():
    res = pd.DataFrame()
    for year in range(2013,2019):
        for month in range(1,13):
            path = glob.glob('Data/html_data/{}/'.format(year) + '{}.html'.format(month))
    
            for i in path:
                l = pd.read_html(i)
                df = pd.DataFrame(l[2])
                res = pd.concat([res,df])
                res.dropna(subset=['Day'],inplace=True)
                res = res[res.Day != 'Monthly means and totals:']
                res.drop(['RA','SN','TS','FG'],axis=1,inplace=True)
    return res
            
def combine_data():
    features = get_features()
    target = calculate_aqi_2013_2018()
    target_df = pd.DataFrame(target)
    final_dataset = pd.concat([features, target_df.set_index(features.index)], axis=1)
    final_dataset.drop(['Day'],axis=1,inplace=True)
    if not os.path.exists('Data/Final_Data'):
        os.makedirs('Data/Final_Data')
    final_dataset.to_csv(r'C:\Users\tapan\Documents\Tapan\machine_learning_notes\Tapan_ML_Projects\Air_Quality_Index\Data\Final_Data\final_dataset.csv',index=False)
    return final_dataset      
if __name__ == "__main__":
    final_dataset = combine_data()