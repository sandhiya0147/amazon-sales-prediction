import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import joblib

# Load data
df = pd.read_csv("amazon_sales_data 2025.csv")
df = df.dropna(subset=["Category", "Price", "Quantity", "Payment Method"])  # Drop missing

# Features and target
X = df[["Price", "Quantity", "Payment Method"]]
y = df["Category"]

# Encode 'Payment Method'
X = pd.get_dummies(X)

# Encode target labels
label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.2)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save model and label encoder
joblib.dump(model, "model.pkl")
joblib.dump(label_encoder, "label_encoder.pkl")
joblib.dump(X.columns.tolist(), "feature_columns.pkl")
