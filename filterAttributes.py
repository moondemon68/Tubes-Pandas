import pandas as pd
import matplotlib.pyplot as plt

def upordown(row):
    if (row['close']<row['open']):
        return "DOWN"
    elif (row['close']>row['open']):
        return "UP"
    else:
        return "SAME"

df=pd.read_csv("crypto-filtered.csv")
df1=df.loc[:,["symbol","date","open","close","volume","high","low","spread"]]
df1["up/down"]=df1.apply(upordown,axis=1)
print(df1)
df1.to_csv("processed-data.csv")
