import pickle
import os
from django.shortcuts import render

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MODEL_PATH = os.path.join(BASE_DIR, 'heart_disease/ml/model.pkl')
SCALER_PATH = os.path.join(BASE_DIR, 'heart_disease/ml/scaler.pkl')

model = pickle.load(open(MODEL_PATH, 'rb'))
scaler = pickle.load(open(SCALER_PATH, 'rb'))
# Create your views here.
def home(request):
    return render(request, 'home.html', {
        'accuracy': round(accuracy * 100, 2)
    })

def predict(request):
    if request.method == "POST":
        features = {
            "male": float(request.POST['male']),
            "age": float(request.POST['age']),
            "cigsPerDay": float(request.POST['cigsPerDay']),
            "BPMeds": float(request.POST['BPMeds']),
            "prevalentStroke": float(request.POST['prevalentStroke']),
            "diabetes": float(request.POST['diabetes']),
            "totChol": float(request.POST['totChol']),
            "sysBP": float(request.POST['sysBP']),
            "BMI": float(request.POST['BMI']),
            "heartRate": float(request.POST['heartRate']),
            "glucose": float(request.POST['glucose']),
        }

        data = list(features.values())
        scaled_data = scaler.transform([data])

        # Probability of heart disease
        prob = model.predict_proba(scaled_data)[0][1]

        # Decision threshold
        if prob >= 0.3:
            result = f"⚠ High Risk of Heart Disease ({prob*100:.1f}%)"
        else:
            result = f"✅ Low Risk of Heart Disease ({prob*100:.1f}%)"

        # ---------------- EXPLANATION LOGIC ----------------
        reasons = []

        if features["age"] > 55:
            reasons.append("Age is high")

        if features["sysBP"] > 140:
            reasons.append("High systolic blood pressure")

        if features["totChol"] > 240:
            reasons.append("High cholesterol level")

        if features["BMI"] > 30:
            reasons.append("High BMI (obesity)")

        if features["cigsPerDay"] > 10:
            reasons.append("Heavy smoking habit")

        if features["diabetes"] == 1:
            reasons.append("Diabetes present")

        if features["prevalentStroke"] == 1:
            reasons.append("History of stroke")

        if not reasons:
            explanation = "All major health parameters are within safe range."
        else:
            explanation = "Risk factors detected: " + ", ".join(reasons)

        return render(request, 'home.html', {
            'result': result,
            'accuracy': accuracy,
            'explanation': explanation
        })

    
ACCURACY_PATH = os.path.join(BASE_DIR, 'heart_disease/ml/accuracy.pkl')
accuracy = pickle.load(open(ACCURACY_PATH, 'rb'))

