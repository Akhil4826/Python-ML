# Customer Churn Prediction Model

This repository contains a Flask-based web application that predicts customer churn using a pre-trained machine learning model. The project is developed using Python and various data science libraries like Pandas, NumPy, and Scikit-learn.

## Features

- **Prediction:** Given customer data, the model predicts whether a customer is likely to churn.
- **Web Interface:** The project uses Flask to create a web interface for interacting with the model.
- **Pre-trained Model:** The app loads a pre-trained model stored as a `.joblib` file and uses it to make predictions.

## Requirements

The following libraries are required to run the application. Install them using the command:

```bash
pip install -r requirements.txt
```
The dependencies are listed in requirements.txt:
```
Flask==2.0.1
pandas==1.3.3
numpy==1.21.2
scikit-learn==0.24.2
joblib==1.0.1

```
## Setup
Clone this repository:
```
git clone https://github.com/yourusername/churn-prediction-app.git
```
Navigate to the project directory:
```
cd churn-prediction-app

```
Install the required libraries:
```
pip install -r requirements.txt
```
Run the Flask application:
```
python app.py

```

Open your browser and navigate to http://127.0.0.1:5000 to access the web interface.

## Model Information
The pre-trained model is stored in the scaler.joblib file, which is loaded when the Flask app is launched. This model has been trained using customer data to predict churn based on various features.

## Files
app.py: The main Flask application file.

requirements.txt: Lists the dependencies required for the project.

scaler.joblib: Pre-trained machine learning model.

## Usage
Input customer data into the web interface and submit the form.
The model will output whether the customer is likely to churn.
