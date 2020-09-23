from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.techindicators import TechIndicators
from alpha_vantage.sectorperformance import SectorPerformances
from alpha_vantage.cryptocurrencies import CryptoCurrencies
import matplotlib
import matplotlib.pyplot as plt
import os
#import pyspark
#from pyspark.sql import  SparkSession
import pandas as pd
# import pylab 
# import scipy.stats as stats
# Make plots bigger
matplotlib.rcParams['figure.figsize'] = (20.0, 10.0)
# import api key
from api.api_key import API_KEY

# load data
compagnys = ['ibm', 'tsla', 'msft', 'tot', 'aal']
compagny = ['ibm', 'tsla', 'msft', 'tot', 'aal']

for i in range(len(compagnys)):
    ts = TimeSeries(key=API_KEY, output_format='pandas')
    compagnys[i], meta_data = ts.get_intraday(symbol=f"{compagny[i]}",interval='1min', outputsize='full')
    compagnys[i] = compagnys[i].rename(columns={"1. open": "open", "2. high": "high", "3. low": "low", "4. close": "close", "5. volume": "volume"})
    compagnys[i] = compagnys[i].to_csv(f"dataset/{compagny[i]}.csv", encoding='utf-8')
    print(f"loading {compagny[i]} Done!...")


# create dataset
ibm = pd.read_csv("dataset/ibm.csv")
tsla = pd.read_csv("dataset/tsla.csv")
msft = pd.read_csv("dataset/msft.csv")
total = pd.read_csv("dataset/tot.csv")
aal = pd.read_csv("dataset/aal.csv")