# -*- coding: utf-8 -*-
"""
Created on Sat Oct 22 23:16:57 2022

@author: John
"""

import pandas as pd

# load 2014 and 2015 csv, and set column 0 as index column
data_2014 = pd.read_csv('2014.csv',index_col=0)
data_2015 = pd.read_csv('2015.csv',index_col=0)

# Create a concate function to check two datas whether has same column names 
# and concate them together
def data_concate(data1,data2):
    tot_cols = len(data1.columns)
    has_same_cols = True
    for col_index in range (0,tot_cols):
        if data1.columns[col_index] != data2.columns[col_index]:
            has_same_cols = False
    if has_same_cols == True:
        result = pd.concat([data1,data2])
    return result

# concate them and output the csv
data_concate(data_2014, data_2015).to_csv('output.csv')