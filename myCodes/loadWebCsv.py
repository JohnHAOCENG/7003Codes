import numpy as np
import pandas as pd

# flights = pd.read_csv("http://rcs.bu.edu/examples/python/data_analysis/flights.csv")

# print(flights.dropna(thresh=14))

s1 = pd.Series([1,2,np.nan])
s2 = pd.DataFrame(np.array([[np.nan,2,np.nan,0],
                  [3,4,np.nan,1],
                  [np.nan,np.nan,np.nan,5],
                  [np.nan,3,np.nan,4]]),
                  columns=["A", "B", "C" ,"D"])

# print(s1.dropna(axis=0))
#
# print(s1.fillna(0))
#
# print(s1.fillna(method='ffill'))
print(s2)
print(s2.fillna(method='ffill', limit=1))
print(s2.fillna(method='ffill', limit=2))