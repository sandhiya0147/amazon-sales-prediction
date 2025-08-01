from flask import Flask, render_template, request
import joblib
import pandas as pd
import os

# Initialize Flask app
app = Flask(__name__)

# Load trained model and encoders
model = joblib.load("model.pkl")
encoder = joblib.load("label_encoder.pkl")
columns = joblib.load("feature_columns.pkl")

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    if request.method == "POST":
        try:
            # Collect input values from form
            price = float(request.form["price"])
            quantity = int(request.form["quantity"])
            payment = request.form["payment"]

            # Prepare base input dictionary with all columns set to 0
            input_data = {col: 0 for col in columns}

            # Set actual feature values
            input_data["Price"] = price
            input_data["Quantity"] = quantity

            # One-hot encode payment method if the column exists
            payment_col = f"Payment Method_{payment}"
            if payment_col in input_data:
                input_data[payment_col] = 1

            # Build input DataFrame in correct column order
            input_df = pd.DataFrame([[input_data[col] for col in columns]], columns=columns)

            # Predict using the trained model
            result = model.predict(input_df)
            prediction = encoder.inverse_transform(result)[0]

        except Exception as e:
            prediction = f"Error: {str(e)}"

    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    # Bind to 0.0.0.0 and use PORT env variable for Render compatibility
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=False, host="0.0.0.0", port=port)
