from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.techindicators import TechIndicators
from alpha_vantage.sectorperformance import SectorPerformances
from alpha_vantage.cryptocurrencies import CryptoCurrencies
import matplotlib
import matplotlib.pyplot as plt
import os
import pyspark
from pyspark.sql import  SparkSession
import pandas as pd
import pylab 
import scipy.stats as stats
# Make plots bigger
matplotlib.rcParams['figure.figsize'] = (20.0, 10.0)
# import api key
from api_key import API_KEY

ts = TimeSeries(key=API_KEY, output_format='pandas')
ibm, meta_data = ts.get_intraday(symbol='ibm',interval='1min', outputsize='full')
ibm = ibm.rename(columns={"1. open": "open", "2. high": "high", "3. low": "low", "4. close": "close", "5. volume": "volume"})
ibm = ibm.to_csv('ibm.csv', encoding='utf-8', index=False)
print(ibm.head())
# One way of loading additional packages to spark