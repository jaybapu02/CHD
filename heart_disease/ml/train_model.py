import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


# Load dataset
df = pd.read_csv(r"C:\Users\ASUS\OneDrive\Desktop\csvFile\framingham.csv")

# Handle missing values
df.fillna(df.mean(), inplace=True)

# Drop unnecessary columns
df.drop(columns=["education", "diaBP", "currentSmoker", "prevalentHyp"], inplace=True)

# Split input & output
X = df.drop(columns=["TenYearCHD"])
y = df["TenYearCHD"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=5
)

# Scaling
scaler = MinMaxScaler()
X_train_scaled = scaler.fit_transform(X_train)

# Logistic Regression (best for this dataset)
model = LogisticRegression(max_iter=1000)
model.fit(X_train_scaled, y_train)

# Save model & scaler
pickle.dump(model, open("heart_disease/ml/model.pkl", "wb"))
pickle.dump(scaler, open("heart_disease/ml/scaler.pkl", "wb"))

print("✅ Model & Scaler saved successfully")

# Evaluate model
X_test_scaled = scaler.transform(X_test)
y_pred = model.predict(X_test_scaled)
accuracy = accuracy_score(y_test, y_pred)

# Save accuracy
pickle.dump(accuracy, open("heart_disease/ml/accuracy.pkl", "wb"))

print(f"✅ Model Accuracy: {accuracy*100:.2f}%")
