from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)
model = joblib.load("model.pkl")
encoder = joblib.load("label_encoder.pkl")
columns = joblib.load("feature_columns.pkl")

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    if request.method == "POST":
        price = float(request.form["price"])
        quantity = int(request.form["quantity"])
        payment = request.form["payment"]

        # Create input dataframe
        input_dict = {
            "Price": price,
            "Quantity": quantity,
            f"Payment Method_{payment}": 1
        }

        # Add missing columns
        for col in columns:
            if col not in input_dict:
                input_dict[col] = 0

        input_df = pd.DataFrame([input_dict])

        # Predict
        result = model.predict(input_df)
        prediction = encoder.inverse_transform(result)[0]

    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)
