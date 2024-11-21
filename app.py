from flask import Flask, request, render_template
import numpy as np
from joblib import load

# Load the model
model = load('models/model.joblib')

# Create Flask app
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Collect input data from form
    input_data = [
        int(request.form['age']),
        int(request.form['sex']),
        int(request.form['cp']),
        int(request.form['trestbps']),
        int(request.form['chol']),
        int(request.form['fbs']),
        int(request.form['restecg']),
        int(request.form['thalach']),
        int(request.form['exang']),
        float(request.form['oldpeak']),
        int(request.form['slope']),
        int(request.form['ca']),
        int(request.form['thal'])
    ]

    # Make prediction
    prediction = model.predict([input_data])
    result = "Heart Disease Detected" if prediction[0] == 1 else "No Heart Disease Detected"

    # Pass the result to the template
    return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
