# 🧠 ML Winter ARC 2025 — Week 1

## Boston Housing Price Prediction (Flask + Scikit-Learn + Render Deployment)

Welcome to **Week 1** of my **ML Winter ARC 2025** journey!  
This week focuses on building, training, and deploying a complete **Machine Learning web application** using Flask and Render.

The project demonstrates a full end-to-end ML workflow — from data preprocessing to deploying a prediction API.

---

## 🚀 Project Overview

This is a **web-based ML app** that predicts **Boston Housing Prices** using a trained **Scikit-Learn model**.  
The app is deployed live at:

👉 **https://mlwinterarc251.onrender.com/**

Users can input values like number of rooms, crime rate, property tax, etc., and get a predicted house price instantly.

---

## 📁 Folder Structure

```
MLwinterARC25/
│
├── week1/
│   ├── app.py                  # Flask backend
│   ├── boston_model.pkl        # Trained ML model
│   ├── scaler.pkl              # Preprocessing scaler
│   ├── boston.csv              # Dataset used
│   ├── templates/
│   │   └── home.html           # Frontend UI
│   ├── Dockerfile              # (Optional) Docker setup
│   └── README.md               # Project documentation
│
├── Procfile                    # Tells Render how to run the app
├── requirements.txt            # App dependencies
└── .github/workflows/…         # (Optional) CI/CD files
```

---

## 🔧 Tech Stack Used

### **Backend**

- Python 3.13
- Flask
- Gunicorn (Render web server)

### **Machine Learning**

- Scikit-learn
- Pandas
- NumPy
- StandardScaler

### **Deployment**

- Render Web Service
- Procfile-based deployment
- Lightweight requirements.txt (no heavy Rust-based packages)

---

## 🧩 Model Details

- **Algorithm:** Linear Regression
- **Dataset:** Boston Housing Dataset (`boston.csv`)
- **Preprocessing:**
  - Missing value handling
  - Feature Scaling using `StandardScaler`
- **Model Artifacts Saved as:**
  - `boston_model.pkl`
  - `scaler.pkl`

These files are loaded automatically when the Flask app starts.

---

## 🌐 How the Flask App Works

### **Entry Route**

```python
@app.route('/')
def home():
    return render_template('home.html')
```

This renders the HTML form where users input housing features.

### **Prediction Route**

```python
@app.route('/predict', methods=['POST'])
```

This:

1. Takes user inputs
2. Applies the saved scaler (`scaler.pkl`)
3. Passes scaled values into the model (`boston_model.pkl`)
4. Returns the final predicted price

---

## 🔥 Deployment on Render — Summary

### Required Files:

```
Procfile
requirements.txt
week1/app.py
week1/templates/home.html
week1/boston_model.pkl
week1/scaler.pkl
```

### **Procfile**

```
web: gunicorn week1.app:app
```

### **Build Command (Render Dashboard)**

```
pip install -r requirements.txt
```

### **Start Command (Render Dashboard)**

```
gunicorn week1.app:app
```

### Important Notes:

- Requirements must be **lightweight** to avoid Rust cargo build failures
- All model files must be inside `week1/`
- App must be served using gunicorn

---

## 🧪 Testing the Deployed App

1. Open the website
2. Enter all housing feature inputs
3. Click **Predict**
4. View the final estimated price

The UI is simple, clean, and responsive.

---
