# ❤️ Coronary Heart Disease Prediction

A **Django-based web application** that uses **Machine Learning** to predict the risk of Coronary Heart Disease (CHD). The model analyzes user input data and provides predictions along with insights.

---

## 🚀 Features

* ❤️ Predicts heart disease risk using ML model
* 🧠 Trained model with preprocessing (scaler + accuracy tracking)
* 🌐 Web interface built using Django
* ⚡ Fast and simple prediction system
* 📊 Displays prediction results dynamically

---

## 🏗️ Project Structure

```bash id="v8c2lm"
Coronary_Heart_Disease/
│
├── manage.py
├── db.sqlite3
├── requirements.txt
│
├── chd/                      # Main Django project
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── heart_disease/            # Core application
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── admin.py
│   │
│   ├── ml/                  # Machine Learning files
│   │   ├── model.pkl
│   │   ├── scaler.pkl
│   │   ├── accuracy.pkl
│   │   └── train_model.py
│   │
│   ├── templates/
│   │   └── home.html
│   │
│   └── migrations/
│
└── .git/
```

*(Structure based on your project files )*

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```bash id="h3k9dx"
git clone https://github.com/your-username/Coronary_Heart_Disease.git
cd Coronary_Heart_Disease
```

### 2️⃣ Create virtual environment

```bash id="y7p1qa"
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
```

### 3️⃣ Install dependencies

```bash id="c8l5wp"
pip install -r requirements.txt
```

### 4️⃣ Run migrations

```bash id="z6t2vn"
python manage.py migrate
```

### 5️⃣ Start the server

```bash id="k1r8us"
python manage.py runserver
```

Open in browser:

```id="m9e4bf"
http://127.0.0.1:8000/
```

---

## 🧠 Machine Learning Details

* Model trained using structured health dataset
* Data preprocessing handled using **StandardScaler**
* Model saved using `.pkl` files
* Accuracy stored for evaluation

---

## 📊 Tech Stack

* **Backend:** Django (Python)
* **Machine Learning:** Scikit-learn
* **Frontend:** HTML, CSS
* **Database:** SQLite

---

## 📌 Future Improvements

* Add more advanced ML models for better accuracy
* Improve UI/UX design
* Add user authentication system
* Deploy on cloud (Render / AWS)

---

## 👨‍💻 Author

**Jaychandra Das**

---

## ⭐ Contribution

Contributions are welcome! Feel free to fork and improve.

---

## 📄 License

This project is for educational purposes.
