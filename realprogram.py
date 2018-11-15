import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("processed-data.csv",index_col=0)
pd.set_option('float_format', '{:f}'.format)    #Mengubah penulisan angka sehingga tidak dalam bentuk saintifik
df.set_index('date', inplace=True)  #Menjadikan atribut "date" sebagai index data

#Chart BTC
btc=df.loc[df["symbol"]=="BTC"];
btc.plot(kind="line",y="close",title="Close Price BTC 2016 - 2018")
plt.xlabel("Tahun")
plt.ylabel("Harga")
plt.xticks([w*365 for w in range(3)],[2016+w for w in range(3)])
plt.show()
print(btc.describe())

#Chart ETH
eth=df.loc[df["symbol"]=="ETH"];
eth.plot(kind="line",y="close",title="Close Price ETH 2016 - 2018")
plt.xlabel("Tahun")
plt.ylabel("Harga")
plt.xticks([w*365 for w in range(3)],[2016+w for w in range(3)])
plt.show()

#Chart Semua Crypto
df.groupby("symbol")["close"].plot(kind="line",stacked=False,logy=False,legend=True,title="Crypto Close Price 2016-2018")
plt.xlabel("Tahun")
plt.ylabel("Harga")
plt.xticks([w*365 for w in range(3)],[2016+w for w in range(3)])
plt.legend(bbox_to_anchor=[1,0.65],loc="center")
plt.show()

#Chart Semua Crypto (Logaritmik)
df.groupby("symbol")["close"].plot(kind="line",stacked=False,logy=True,legend=True,title="Crypto Close Price 2016-2018 (Logaritmik)")
plt.xlabel("Tahun")
plt.ylabel("Harga")
plt.xticks([w*365 for w in range(3)],[2016+w for w in range(3)])
plt.legend(bbox_to_anchor=[1,0.65],loc="center")
plt.show()

#Stacked Bar Chart Naik Turunnya Harga Crypto Per Hari
df.groupby(["symbol","up/down"]).size().unstack().plot(kind="bar",stacked=True,title="Naik Turunnya Harga Crypto Per Hari")
plt.xlabel("Mata Uang")
plt.ylabel("Banyaknya Hari")
plt.show()
