<<<<<<< HEAD
from flask import Flask, jsonify, request, render_template
from flask_restful import Resource, Api, reqparse
#from sklearn.feature_extraction.text import TfidfVectorizer, TfidfTransformer, CountVectorizer
#from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import pandas as pd

from viz import ibm, tsla, total, msft

#from ..opt.workspace.set import data

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

# print(f'server est lancé sur le port {port}')
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
=======
from flask import Flask, render_template, jsonify
import json
# import requests
app = Flask(__name__)

# import 
from viz import ibm


 

# route 
@app.route('/')
def index():
    message = ibm.head()

    # affichage
    return render_template('index.html', title='home', message=message)

#@app.route('/api/')
#def api():
    # response = requests.get(API_KEY)
    # content = json.loads(response.content.decode('utf-8'))

    # if response.status_code != 200:
    #     return jsonify({
    #        'status': 'error',
    #        'message': 'La requête à l\'API  n\'a pas fonctionné. Voici le message renvoyé par l\'API : {}'.format(content['message'])
    #    }), 500

    # affichage
    #return render_template('page.html', title='Acceuil', content=content)

# create port
port = 5000
# print(f'server est lancé sur le port {port}')
if __name__ == '__main__':
    app.run(host='0.0.0.0',port= port, debug=True)
>>>>>>> 38e5e47926bdc43b745a6149b008facdf55d436b
