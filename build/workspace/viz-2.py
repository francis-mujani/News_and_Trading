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

from api_key import API_KEY



# ts = TimeSeries(key=API_KEY, output_format='pandas')
# ibm, meta_data = ts.get_intraday(symbol='ibm',interval='1min', outputsize='full')

# ibm = ibm.rename(columns={"1. open": "open", "2. high": "high", "3. low": "low", "4. close": "close", "5. volume": "volume"})

# ibm = ibm.to_csv('ibm.csv', encoding='utf-8', index=False)

# One way of loading additional packages to spark
os.environ['PYSPARK_SUBMIT_ARGS'] = '--packages org.mongodb.spark:mongo-spark-connector_2.11:2.2.0 pyspark-shell'

# ********************** Recuperation des données depuis la base de donné mongodb*******************************
#                                  - convert collection database in pandas

def get_df(name):

    spark = pyspark.sql.SparkSession.builder\
        .appName('test-mongo')\
        .config("spark.mongodb.input.uri", "mongodb://my-mongo/trading."+name) \
        .config("spark.mongodb.output.uri", "mongodb://my-mongo/trading."+name ) \
        .getOrCreate()
     
    sc = spark.sparkContext
    rdd = spark.read.format("com.mongodb.spark.sql.DefaultSource").load()
    df = rdd.select("*").toPandas()
    print(f"convert {name} done...")
    return df


ibm = get_df('ibm')
print(ibm.head())
# ibm.index = pd.to_datetime(ibm.date)
# ibm.drop(['date','_id'], axis=1, inplace=True)
# print(ibm.head)

# create dictionaire
# NAME = ["TOTAL", "TSLA", "IBM","MSFT" ]
# data = {k:get_df(k) for k in NAME}

# create data
# ibm = data['IBM']
# total = data['TOTAL']
# msft = data['MSFT']
# tsla = data['TSLA']

# changer l'index en datetime
# compagnys = [ibm,total, msft,tsla]
# for compagny in compagnys:
#     compagny.index = pd.to_datetime(compagny.date)
#     compagny.drop(['date','_id'], axis=1, inplace=True)
# viz_total = total.head()

# plotting all data columns [close]
# compagnys_liste = ["IBM","TOTAL", "MSFT","TSLA"]
# for i, compagny in enumerate(compagnys):
#     plt.plot(compagny.index, compagny['close'])
#     plt.title(compagnys_liste[i])
#     plt.xlabel('Year')
#     plt.ylabel('Price')
#     plt.legend(compagnys_liste[i])
#     plt.show()


# Vérifier la distribution normale
# for i in range(len(compagnys)):
#     compagnys[i]['prix_chg'] = compagnys[i]['close'].pct_change()[1:]
#     compagny.dropna(inplace=True, axis=0)
#     stats.probplot(compagnys[i]['prix_chg'], dist="norm", plot=pylab)
