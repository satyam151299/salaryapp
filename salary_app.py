#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask,request, url_for, redirect, render_template
import pickle
from flask_sqlalchemy import SQLAlchemy
from flask_mysqldb import MySQL
import numpy as np
app = Flask(__name__)

model = pickle.load(open('model1.pkl', 'rb'))
@app.route('/')
def home():
    return render_template('index1.html')
@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [x for x in request.form.values()]
    final_features=[]
    for i in range(len(int_features)):
        if(i>=2):
            final_features.append(int(int_features[i]))
    print(final_features)  
    final_fe = [np.array(final_features)]
    print(final_fe)
    prediction = model.predict(final_fe)

    output = round(prediction[0], 2)

    return render_template('index1.html', prediction_text='Employee Salary should be $ {}'.format(output))
if __name__ == "__main__":
    app.run()


# In[ ]:




