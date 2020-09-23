from flask import Flask, jsonify, request, render_template
from flask_restful import Resource, Api, reqparse
import numpy as np
import pandas as pd
import os
import time


# import dataset
# from load import ibm, tsla, total, msft, aal


compagnys = ["Ibm", "Tsla", "Total", "Msft" ]
# import netifaces
# import platform
app = Flask(__name__)

# route 
@app.route('/')
def index():

    # affichage
    return render_template('index.html', title='home', compagnys = compagnys)


@app.route('/ibm')
def Ibm():

    # affichage
    return render_template('ibm.html', title='home')


# create port
port = int(os.environ.get("PORT", 5000))

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=port)

