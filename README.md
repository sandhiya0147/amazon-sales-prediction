# Amazon Sales Predictor

This project predicts Amazon product sales using th **Random Forest classifier**, trained on historical sales data. A Flask web app allows users to input product features and view predicted sales instantly.

---

## Features

- Simple web form to enter product details.
- Shows sales prediction instantly after submission.
- Trained on historical Amazon sales data for accuracy.
- Uses a saved machine learning model for fast predictions.
- Easy to customize and extend with new features.


---

## Prerequisites

Make sure the following are installed:

- Python 3.7 or higher installed
- Git installed and configured
- Basic knowledge of Python and Flask
- A GitHub account (for code hosting)
- Render account (for deployment)

---

## Installation

### 1. Clone the repository

```
git clone https://github.com/sandhiya0147/amazon-sales-prediction.git
cd amazon-sales-prediction
```

### 2. Install dependencies

```
pip install -r requirements.txt
```

---

## Running the Application

Start the Flask development server:

```
python app.py
```

Then open your browser and go to:

```
http://127.0.0.1:5000
```

---

## How It Works

- The user opens the web app and enters product information in the form.
- The app collects and preprocesses the input data to match the training format.
- The processed data is passed to a trained Random Forest model.
- The model predicts the expected number of sales for the product.
- The predicted sales value is shown instantly on the web page.

---

## File Structure

```
amazon-sales-predictor/
│
├── app.py                          
├── model_train.py                  
├── amazon_sales_data 2025.csv      
├── model.pkl                       
├── feature_columns.pkl             
├── label_encoder.pkl               
├── requirements.txt               
├── README.md                       
│
├── templates/
│   └── index.html                  
├── assets/                        
│   ├── input_form.png
│   ├── filled_input.png
│   └── predicted_result.png
```

---

## Future Improvements

- Add more features like shipping time, seller type, and seasonality to improve prediction accuracy.
- Support multiple ML models and allow users to choose between them (e.g., XGBoost, Gradient Boosting).
- Enable file upload for batch predictions from CSV files.
- Integrate data visualization to show sales trends and model performance.
- Deploy a mobile-friendly version for better accessibility on smartphones and tablets.

---



## Step-by-Step Guide: How to Use the Movie Interest Predictor


### Step 1: Input Form
![Form](assests/input_form.png)  

### Step 2: Filled Form 
![Prediction Result](assests/filled_input.png)  

### Step 3: Prediction Result
![Full Page](assests/predicted_result.png)

---

## Live Demo

[Click here to view the deployed app](https://amazon-sales-prediction.onrender.com)

---
