# 🏢 Employee Attrition Predictor

A machine learning–powered web application that predicts whether an employee is likely to leave a company based on key HR metrics. Built with **Flask** and **scikit-learn**, deployed on **Render**.

🔗 **Live Demo:** [https://employee-attrition-rtvm.onrender.com](https://employee-attrition-rtvm.onrender.com)

---

## 📌 Overview

Employee attrition is a critical concern for HR departments. This app helps organizations proactively identify at-risk employees by analyzing 28 HR attributes — from compensation and job role to work-life balance and tenure — and returning an instant prediction.

---

## ✨ Features

- 🔍 Predicts employee attrition risk (**Likely to Leave** / **Likely to Stay**)
- 📋 Accepts 28 employee attributes across 4 categories:
  - **Personal** — Gender, Marital Status, Education, Distance from Home
  - **Job** — Department, Job Role, Overtime, Satisfaction Scores, Stock Options
  - **Compensation** — Daily/Hourly/Monthly Rate, Salary Hike
  - **Experience** — Total Working Years, Years at Company, Promotions, Manager Tenure
- ⚡ Real-time prediction via a clean, responsive web UI
- 🚀 Deployed and accessible via a public URL

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python, Flask |
| ML Model | scikit-learn (trained & serialized with `pickle`) |
| Data Processing | pandas |
| Frontend | HTML5, CSS3 (Vanilla), Google Fonts (Inter) |
| Server | Gunicorn |
| Deployment | Render |

---

## 📂 Project Structure

```
employee/
├── app.py                                      # Flask application & prediction route
├── employee_attrition.pkl                      # Trained ML model (pickled)
├── notebbok.ipynb                              # EDA & model training notebook
├── WA_Fn-UseC_-HR-Employee-Attrition.csv       # IBM HR Analytics dataset
├── requirements.txt                            # Python dependencies
├── templates/
│   └── index.html                              # Frontend UI (Jinja2 template)
└── static/
    └── style.css                               # Application styles
```

---

## 📊 Dataset

- **Source:** [IBM HR Analytics Employee Attrition & Performance](https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset) — provided via Kaggle
- **Records:** 1,470 employees
- **Target Variable:** `Attrition` (Yes / No)
- **Features Used:** 28 HR attributes (personal, job, compensation, experience)

---

## 🚀 Getting Started (Run Locally)

### Prerequisites

- Python 3.8+
- pip

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/your-username/employee-attrition.git
cd employee-attrition

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the Flask development server
python app.py
```

Then open your browser and navigate to `http://127.0.0.1:5000`.

---

## 🧠 Model

The ML model was trained in `notebbok.ipynb` using the IBM HR Analytics dataset. The notebook covers:

- Exploratory Data Analysis (EDA)
- Feature engineering & preprocessing
- Model training and evaluation
- Serialization of the final model to `employee_attrition.pkl`

The Flask app loads this pickle file at startup and uses it to serve real-time predictions.

---

## 📡 Deployment

The app is deployed on **Render** using **Gunicorn** as the production WSGI server.

- **Live URL:** [https://employee-attrition-rtvm.onrender.com](https://employee-attrition-rtvm.onrender.com)
- Render auto-deploys on every push to the connected GitHub branch.

> **Note:** The free-tier Render instance may spin down after inactivity. The first request after a cold start may take ~30–60 seconds.

---

## 📦 Dependencies

```
flask
pandas
scikit-learn
gunicorn
joblib
```

Install all dependencies via:

```bash
pip install -r requirements.txt
```

---

## 🙌 Acknowledgements

- Dataset: [IBM HR Analytics — Kaggle](https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset)
- Hosted on: [Render](https://render.com)
