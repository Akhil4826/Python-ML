from flask import Flask, request, jsonify
import numpy as np
import pandas as pd
import pickle
import joblib






# Initialize the Flask app
app = Flask(__name__)

# Load the pre-trained model and the scaler without using open()
model = joblib.load('Python Notebooks/random_forest_model.joblib')
scaler = joblib.load('Python Notebooks/scaler.joblib')

# Define the prediction route
@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()  # Get data from the POST request
    features = data['features']  # Extract the features
    
    # Convert the features to a DataFrame and scale them
    features_df = pd.DataFrame([features], columns=['Store', 'Holiday_Flag', 'Temperature', 'Fuel_Price', 'CPI', 'Unemployment'])
    scaled_features = scaler.transform(features_df)
    
    # Make predictions using the loaded model
    prediction = model.predict(scaled_features)[0]
    
    # Return the prediction as a JSON response
    return jsonify({'predicted_sales': prediction})

# Define the home route
@app.route('/')
def home():
    return "Welcome to the Walmart Sales Prediction API"

# Run the app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)



