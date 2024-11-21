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
    try:
        # Get input from form
        data = [float(request.form[param]) for param in [
            'age', 'sex', 'cp', 'trestbps', 'chol', 
            'fbs', 'restecg', 'thalach', 'exang', 
            'oldpeak', 'slope', 'ca', 'thal'
        ]]
        
        # Convert to numpy array and predict
        prediction = model.predict([data])[0]
        result = "Heart Disease Detected" if prediction == 1 else "No Heart Disease"
        return render_template('result.html', result=result)
    
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == '__main__':
    app.run(debug=True)
