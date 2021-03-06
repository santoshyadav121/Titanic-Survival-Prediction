# -*- coding: utf-8 -*-
"""app.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ZzksCVZvWU6pqut0tZY8o7yOuoll1eMB
"""




from flask import Flask, request, jsonify, render_template
import random
import numpy as np
import os
import pickle

# cd /content/drive/MyDrive/ML/ML Projects/Titanic Survival/

app = Flask(__name__)
model = pickle.load(open('titanic_survival.pkl','rb'))

@app.route('/')
def hello():
  return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():    
    input = [x for x in request.form.values()]
    # input = [float(j) if i ==5 else j for i,j in enumerate(input)]
    print(input)
    test_data = np.array(input).reshape(1,-1)
    y_pred = model.predict(test_data)[0]
    if y_pred == 0:
      text = 'ohh!! no , this person didn\'t survived titanic incident'
    else:
      text = 'congrats!!!  this person survived titanic incident'

    return render_template('output.html', prediction_text = text)

if __name__ == '__main__':
  app.run()