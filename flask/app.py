from flask import Flask, jsonify, request, render_template
from flask_restful import Resource, Api, reqparse
import numpy as np
import pandas as pd
import os

# import dataset
from viz import ibm, tsla, total, msft



# ibm = data['Ibm']
# total = data['Total']
# msft = data['Msft']
# tsla = data['Tsla']
close = np.array(ibm["close"])
date = ibm["date"]
listes = [ibm.head(), tsla.head(), total.head(), msft.head()]
compagnys = ["Ibm", "Tsla", "Total", "Msft" ]
# import netifaces
# import platform
app = Flask(__name__)

# route 
@app.route('/')
def index():

    # affichage
    return render_template('index.html', title='home', listes=listes, compagnys = compagnys, close=close, date=date)


@app.route('/ibm')
def ibm():

    # affichage
    return render_template('ibm.html', title='home', imb=ibm)


# create port
port = int(os.environ.get("PORT", 5000))

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=port)

