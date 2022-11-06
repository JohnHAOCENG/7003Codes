import pandas as pd
import numpy as np

df = pd.read_csv("data.csv",index_col=0)

df = df[df["lct"]>0]
df = df[df["act"]>0]
df = df[df["prcc_f"]>0]
df = df[df["ni"]>0]
df = df[df["csho"]>0]

df = df.dropna(axis=0, how="any")

CLR = (df["lct"]/df["act"])

PE = df["prcc_f"]/(df["ni"]/df["csho"])

print(PE.describe())