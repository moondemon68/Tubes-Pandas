import pandas as pd
import matplotlib.pyplot as plt

# SUMBER
# https://www.kaggle.com/jessevent/all-crypto-currencies

df=pd.read_csv("crypto-markets.csv")
df1=df.loc[((df["symbol"]=="BTC") | (df["symbol"]=="ETH") | (df["symbol"]=="XLM")
| (df["symbol"]=="XRP") | (df["symbol"]=="LTC")) & (df["date"]>="2016")]
df1.to_csv("crypto-filtered.csv")
