# 📊 **Customer Churn Prediction Model** 

![Customer Churn Prediction](https://github.com/user-attachments/assets/17a66874-39e5-45a2-af34-ad909a437935)

This repository contains a **Sales Predictor** that predicts customer churn using a pre-trained machine learning model. The project is developed using **Python** and various data science libraries like **Pandas**, **NumPy**, and **Scikit-learn**.


---

## 📊 **Project Goal**

The goal of this project was to analyze the available data and build a model that could predict weekly sales with high accuracy.

---

## 📋 **Data Description**
The dataset contains the following key features:
- **Store:** Store number
- **Date:** Sales week start date
- **Weekly_Sales:** Store week sales
- **Holiday_Flag:** Indicates the presence or absence of a holiday
- **Temperature:** Air temperature in the region
- **Fuel_Price:** Fuel cost in the region
- **CPI:** Consumer price index
- **Unemployment:** Unemployment rate

---

## 🌟 **Features**
- **🔍 Prediction:** Given customer data, the model predicts whether a customer is likely to churn.
- **🌐 Web Interface:** The project uses Flask to create a web interface for interacting with the model.
- **💾 Pre-trained Model:** The app loads a pre-trained model stored as a `.joblib` file and uses it to make predictions.

---

## 📋 **Requirements**

The following libraries are required to run the application. Install them using the command:

```bash
pip install -r requirements.txt
```

### **Dependencies**:
The dependencies are listed in `requirements.txt`:
```
Flask==2.0.1
pandas==1.3.3
numpy==1.21.2
scikit-learn==0.24.2
joblib==1.0.1
```

---

## ⚙️ **Setup**
To set up the project locally, follow these steps:

1. **Clone this repository:**
   ```bash
   git clone https://github.com/yourusername/churn-prediction-app.git
   ```
   
2. **Navigate to the project directory:**
   ```bash
   cd churn-prediction-app
   ```

3. **Install the required libraries:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Flask application:**
   ```bash
   python app.py
   ```

5. **Access the application:**
   Open your browser and navigate to [http://127.0.0.1:5000](http://127.0.0.1:5000) to access the web interface. 

---

## 📈 **Model Information**
The pre-trained model is stored in the `scaler.joblib` file, which is loaded when the Flask app is launched. This model has been trained using customer data to predict churn based on various features, including:
- **Customer Age**
- **Monthly Charges**
- **Total Charges**
- **Contract Type**
- **Payment Method**

---

## 📂 **Files**
- **`app.py`**: The main Flask application file.
- **`requirements.txt`**: Lists the dependencies required for the project.
- **`scaler.joblib`**: Pre-trained machine learning model.

---

## 👩‍💻 **Usage**
1. Input customer data into the web interface and submit the form.
2. The model will output whether the customer is likely to churn, helping businesses make informed decisions.

---

## 🎨 **Visuals**
### Sample Interface
![Sample Interface](https://via.placeholder.com/800x400.png?text=Sample+Web+Interface)

### User Interaction Flow
![User Interaction Flow](https://via.placeholder.com/800x400.png?text=User+Interaction+Flow)

---

## 🤝 **Contributing**
Contributions are welcome! If you have suggestions for improvements, feel free to fork the repository and submit a pull request. 

---


### 🌐 **Contact**
For inquiries or feedback, please contact:  
- **Email**: akhilteotia19@gmail.com 
- **GitHub**: [Akhil4826](https://github.com/Akhil4826)

---

---
## Snapshot of the prediction model

![Screenshot 2024-10-06 214135](https://github.com/user-attachments/assets/24cbdff6-86fb-46d3-a1f9-d29de59c544b)

---

### 🚀 **Start Your Journey with Customer Churn Prediction!**
Explore the power of predictive analytics and enhance customer retention strategies with our easy-to-use platform. 🌟


