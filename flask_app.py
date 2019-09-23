
# A very simple Flask Hello World app for you to get started with...

# Import libraries
import numpy as np
import pandas as pd
from flask import Flask, request, jsonify, render_template
#import pickle
from sklearn.externals import joblib

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'HELLO GENGZ. LETS PREDICT YOUR CREDIT SCORING >> <a href="https://github.com/hmaghfira/Analytic-Model-Deployment">GITHUB</a>'

# Load the model
model = joblib.load(open('/home/hmaghfira/mysite/random_forest.pkl','rb'))

@app.route('/api',methods=['POST'])
def predict():
    datas = request.get_json(force=True)
    pred = []
    for data in datas:
        # Make prediction using model loaded from disk as per the data.
        prediction = model.predict([np.array([data["LIMIT_BAL"], data["PAY_1"], data["AGE"], data["EDUCATION"], data["SEX"]])])

        # Take the first value of prediction
        output = int(prediction[0])
        out = "Terlambat" if output==1 else "Tidak Terlambat"
        pred.append(out)

    return jsonify(pred)