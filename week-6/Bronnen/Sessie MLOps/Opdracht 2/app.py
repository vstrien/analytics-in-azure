from pycaret.regression import *
import pandas as pd
import numpy as np
from flask import Flask,request, url_for, redirect, render_template, jsonify
import pickle

app = Flask(__name__)
model=load_model('deployment_28042020')

@app.route('/predict',methods=['POST'])
def predict():
    int_features=[x for x in request.form.values()]
    final=np.array(int_features)
    col = ['age', 'sex', 'bmi', 'children', 'smoker', 'region']
    data_unseen = pd.DataFrame([final], columns = col)
    print(int_features)
    print(final)
    prediction=predict_model(model, data=data_unseen, round = 0)
    prediction=int(prediction.Label[0])
    return render_template('home.html',pred='Verwachte kosten: {}'.format(prediction))

@app.route('/')
def home():
    return render_template("home.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug = True)