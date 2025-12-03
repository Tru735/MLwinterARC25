import pickle
from flask import Flask, request, jsonify, url_for, render_template
import numpy as np
import pandas as pd

app = Flask(__name__)
## load
import os

BASE = os.path.dirname(__file__)

model_path = os.path.join(BASE, 'boston_model.pkl')
scaler_path = os.path.join(BASE, 'scaler.pkl')

model = pickle.load(open(model_path, 'rb'))
scaler = pickle.load(open(scaler_path, 'rb'))
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict', methods=['POST'])

def predict():
    data = request.json['data']
    print(data)
    print((np.array(list(data.values())).reshape(1,-1)))
    new_data = scaler.transform(np.array(list(data.values())).reshape(1,-1))
    model_pred = model.predict(new_data)
    return jsonify({'prediction': model_pred[0]})

@app.route('/predict_form', methods=['POST'])

def predict_form():
    values = list(request.form.values())
    data_form = [float(v) for v in values]
    final_input = scaler.transform(np.array(data_form).reshape(1,-1))
    print(final_input)
    model_final_pred = f'{model.predict(final_input)[0]:.2f}'
    return render_template('home.html', prediction_text="Predicted House Price is {}.".format(model_final_pred))

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = int(os.environ.get("PORT",5000)), debug=True)
    
    