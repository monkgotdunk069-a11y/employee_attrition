import os
from flask import Flask, render_template, request
import pandas as pd
import pickle

app = Flask(__name__)
app.config["LIVE_APP_URL"] = os.getenv("LIVE_APP_URL", "https://employee-attrition-rtvm.onrender.com")

with open("employee_attrition.pkl", "rb") as f:
    model = pickle.load(f)

@app.route("/")
def home():
    return render_template("index.html", live_app_url=app.config["LIVE_APP_URL"])

@app.route("/predict", methods=["POST"])
def predict():

    data = {
        "BusinessTravel":[request.form["BusinessTravel"]],
        "DailyRate":[float(request.form["DailyRate"])],
        "Department":[request.form["Department"]],
        "DistanceFromHome":[float(request.form["DistanceFromHome"])],
        "Education":[float(request.form["Education"])],
        "EducationField":[request.form["EducationField"]],
        "EnvironmentSatisfaction":[float(request.form["EnvironmentSatisfaction"])],
        "Gender":[request.form["Gender"]],
        "HourlyRate":[float(request.form["HourlyRate"])],
        "JobInvolvement":[float(request.form["JobInvolvement"])],
        "JobLevel":[float(request.form["JobLevel"])],
        "JobRole":[request.form["JobRole"]],
        "JobSatisfaction":[float(request.form["JobSatisfaction"])],
        "MaritalStatus":[request.form["MaritalStatus"]],
        "MonthlyIncome":[float(request.form["MonthlyIncome"])],
        "MonthlyRate":[float(request.form["MonthlyRate"])],
        "NumCompaniesWorked":[float(request.form["NumCompaniesWorked"])],
        "OverTime":[request.form["OverTime"]],
        "PercentSalaryHike":[float(request.form["PercentSalaryHike"])],
        "PerformanceRating":[float(request.form["PerformanceRating"])],
        "RelationshipSatisfaction":[float(request.form["RelationshipSatisfaction"])],
        "StockOptionLevel":[float(request.form["StockOptionLevel"])],
        "TotalWorkingYears":[float(request.form["TotalWorkingYears"])],
        "TrainingTimesLastYear":[float(request.form["TrainingTimesLastYear"])],
        "WorkLifeBalance":[float(request.form["WorkLifeBalance"])],
        "YearsAtCompany":[float(request.form["YearsAtCompany"])],
        "YearsInCurrentRole":[float(request.form["YearsInCurrentRole"])],
        "YearsSinceLastPromotion":[float(request.form["YearsSinceLastPromotion"])],
        "YearsWithCurrManager":[float(request.form["YearsWithCurrManager"])]
    }

    df = pd.DataFrame(data)

    prediction = model.predict(df)[0]
    print("RAW PREDICTION:", prediction)

    if prediction == 1 or prediction == "Yes":
        result = "⚠ Employee Likely To Leave"
    else:
        result = "✅ Employee Likely To Stay"

    return render_template(
        "index.html",
        prediction=result,
        live_app_url=app.config["LIVE_APP_URL"]
    )

if __name__ == "__main__":
    app.run(debug=True)