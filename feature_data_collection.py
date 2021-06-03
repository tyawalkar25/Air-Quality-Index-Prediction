# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 23:30:56 2021

@author: tapan
"""

import requests
import os
import sys
import time

def retrieve_air_quality_data():
    for year in range(2016,2021):
        for month in range(1,13):
            if month < 10:
                url = 'https://en.tutiempo.net/climate/0{}-{}/ws-432950.html'.format(month,year)
            else:
                url = 'https://en.tutiempo.net/climate/{}-{}/ws-432950.html'.format(month,year)
                
            data = requests.get(url)
            data_encoded = data.text.encode('utf=8')
        
            if not os.path.exists('Data/html_data/{}'.format(year)):
                os.makedirs('Data/html_data/{}'.format(year))
            with open('Data/html_data/{}/{}.html'.format(year,month),'wb') as output:
                output.write(data_encoded)
            
        sys.stdout.flush()
        

if __name__ == "__main__":
    start_time = time.time()
    retrieve_air_quality_data()
    end_time = time.time()
    print("total time for data collection {}".format(end_time-start_time))
    