from pathlib import Path
import joblib
import pandas as pd


# ============================================================
# PATHS
# ============================================================

BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_DIR = BASE_DIR / "models"


# ============================================================
# LOAD MODEL + ENCODER
# ============================================================

model = joblib.load(
    MODEL_DIR / "attrition_model.pkl"
)

encoder = joblib.load(
    MODEL_DIR / "attrition_encoder.pkl"
)


# ============================================================
# NUMERICAL FEATURES
# ============================================================

NUMERIC_FEATURES = [
    "Age",
    "DailyRate",
    "DistanceFromHome",
    "Education",
    "EmployeeCount",
    "EmployeeNumber",
    "EnvironmentSatisfaction",
    "HourlyRate",
    "JobInvolvement",
    "JobLevel",
    "JobSatisfaction",
    "MonthlyIncome",
    "MonthlyRate",
    "NumCompaniesWorked",
    "PercentSalaryHike",
    "PerformanceRating",
    "RelationshipSatisfaction",
    "StandardHours",
    "StockOptionLevel",
    "TotalWorkingYears",
    "TrainingTimesLastYear",
    "WorkLifeBalance",
    "YearsAtCompany",
    "YearsInCurrentRole",
    "YearsSinceLastPromotion",
    "YearsWithCurrManager",
]


# ============================================================
# HUMAN-READABLE FEATURE NAMES
# ============================================================

FEATURE_LABELS = {
    "Age": "Age",
    "BusinessTravel": "Business Travel",
    "DailyRate": "Daily Rate",
    "Department": "Department",
    "DistanceFromHome": "Distance From Home",
    "Education": "Education",
    "EducationField": "Education Field",
    "EnvironmentSatisfaction": "Environment Satisfaction",
    "Gender": "Gender",
    "JobInvolvement": "Job Involvement",
    "JobLevel": "Job Level",
    "JobRole": "Job Role",
    "JobSatisfaction": "Job Satisfaction",
    "MaritalStatus": "Marital Status",
    "MonthlyIncome": "Monthly Income",
    "NumCompaniesWorked": "Companies Worked",
    "OverTime": "Overtime",
    "PercentSalaryHike": "Salary Hike",
    "PerformanceRating": "Performance Rating",
    "RelationshipSatisfaction": "Relationship Satisfaction",
    "StockOptionLevel": "Stock Options",
    "TotalWorkingYears": "Total Working Years",
    "TrainingTimesLastYear": "Training Frequency",
    "WorkLifeBalance": "Work-Life Balance",
    "YearsAtCompany": "Years At Company",
    "YearsInCurrentRole": "Years In Current Role",
    "YearsSinceLastPromotion": "Years Since Last Promotion",
    "YearsWithCurrManager": "Years With Current Manager",
}


# ============================================================
# RISK DRIVER DETECTION
# ============================================================

def get_risk_drivers(employee: dict):

    drivers = []

    # --------------------------------------------------------
    # OVERTIME
    # --------------------------------------------------------

    if employee.get("OverTime") == "Yes":
        drivers.append({
            "factor": "Overtime",
            "impact": "High",
            "reason": "Frequent overtime can increase workload and burnout risk."
        })


    # --------------------------------------------------------
    # JOB SATISFACTION
    # --------------------------------------------------------

    satisfaction = employee.get("JobSatisfaction")

    if satisfaction is not None:

        if satisfaction <= 2:
            drivers.append({
                "factor": "Job Satisfaction",
                "impact": "High",
                "reason": "Low job satisfaction may indicate employee disengagement."
            })

        elif satisfaction == 3:
            drivers.append({
                "factor": "Job Satisfaction",
                "impact": "Medium",
                "reason": "Job satisfaction is moderate and may require monitoring."
            })


    # --------------------------------------------------------
    # WORK-LIFE BALANCE
    # --------------------------------------------------------

    work_life = employee.get("WorkLifeBalance")

    if work_life is not None:

        if work_life <= 2:
            drivers.append({
                "factor": "Work-Life Balance",
                "impact": "High",
                "reason": "Lower work-life balance can contribute to employee turnover."
            })

        elif work_life == 3:
            drivers.append({
                "factor": "Work-Life Balance",
                "impact": "Medium",
                "reason": "Work-life balance is acceptable but could be improved."
            })


    # --------------------------------------------------------
    # ENVIRONMENT SATISFACTION
    # --------------------------------------------------------

    environment = employee.get("EnvironmentSatisfaction")

    if environment is not None and environment <= 2:
        drivers.append({
            "factor": "Environment Satisfaction",
            "impact": "High",
            "reason": "Low workplace satisfaction may increase attrition risk."
        })


    # --------------------------------------------------------
    # DISTANCE FROM HOME
    # --------------------------------------------------------

    distance = employee.get("DistanceFromHome")

    if distance is not None:

        if distance >= 20:
            drivers.append({
                "factor": "Distance From Home",
                "impact": "High",
                "reason": "Long commuting distance can negatively affect employee retention."
            })

        elif distance >= 10:
            drivers.append({
                "factor": "Distance From Home",
                "impact": "Medium",
                "reason": "The employee has a relatively long commute."
            })


    # --------------------------------------------------------
    # YEARS AT COMPANY
    # --------------------------------------------------------

    years_company = employee.get("YearsAtCompany")

    if years_company is not None and years_company <= 2:
        drivers.append({
            "factor": "Short Tenure",
            "impact": "Medium",
            "reason": "Employees with short tenure may have higher retention uncertainty."
        })


    # --------------------------------------------------------
    # YEARS SINCE PROMOTION
    # --------------------------------------------------------

    years_promotion = employee.get("YearsSinceLastPromotion")

    if years_promotion is not None and years_promotion >= 5:
        drivers.append({
            "factor": "Career Progression",
            "impact": "Medium",
            "reason": "A long period since the last promotion may indicate limited career progression."
        })


    # --------------------------------------------------------
    # JOB INVOLVEMENT
    # --------------------------------------------------------

    involvement = employee.get("JobInvolvement")

    if involvement is not None and involvement <= 2:
        drivers.append({
            "factor": "Job Involvement",
            "impact": "Medium",
            "reason": "Low involvement may indicate reduced engagement with the role."
        })


    # --------------------------------------------------------
    # SORT BY IMPACT
    # --------------------------------------------------------

    priority = {
        "High": 3,
        "Medium": 2,
        "Low": 1
    }

    drivers.sort(
        key=lambda x: priority[x["impact"]],
        reverse=True
    )

    return drivers[:5]


# ============================================================
# HR RECOMMENDATIONS
# ============================================================

def get_recommendations(risk_level, drivers):

    recommendations = []

    factors = [
        driver["factor"]
        for driver in drivers
    ]


    if "Overtime" in factors:
        recommendations.append(
            "Review workload and overtime frequency."
        )


    if "Job Satisfaction" in factors:
        recommendations.append(
            "Schedule an employee satisfaction check-in."
        )


    if "Work-Life Balance" in factors:
        recommendations.append(
            "Discuss workload and work-life balance."
        )


    if "Distance From Home" in factors:
        recommendations.append(
            "Consider flexible or hybrid work options where possible."
        )


    if "Career Progression" in factors:
        recommendations.append(
            "Discuss career growth and promotion opportunities."
        )


    if "Job Involvement" in factors:
        recommendations.append(
            "Explore ways to improve employee engagement and role involvement."
        )


    if not recommendations:

        if risk_level == "Low":
            recommendations.append(
                "Continue regular employee engagement and monitoring."
            )

        elif risk_level == "Medium":
            recommendations.append(
                "Schedule a proactive HR check-in."
            )

        else:
            recommendations.append(
                "Prioritize an HR review of this employee."
            )


    return recommendations[:4]


# ============================================================
# MAIN PREDICTION FUNCTION
# ============================================================

def predict_attrition(employee: dict):

    # --------------------------------------------------------
    # Convert employee dictionary into DataFrame
    # --------------------------------------------------------

    df = pd.DataFrame([employee])


    # --------------------------------------------------------
    # Get categorical features from encoder
    # --------------------------------------------------------

    categorical_features = list(
        encoder.feature_names_in_
    )


    # --------------------------------------------------------
    # Encode categorical features
    # --------------------------------------------------------

    encoded = encoder.transform(
        df[categorical_features]
    )


    encoded_df = pd.DataFrame(
        encoded,
        columns=encoder.get_feature_names_out(
            categorical_features
        )
    )


    # --------------------------------------------------------
    # Find numerical columns expected by model
    # --------------------------------------------------------

    encoded_columns = set(
        encoded_df.columns
    )


    numerical_features = [
        col
        for col in model.feature_names_in_
        if col not in encoded_columns
    ]


    numerical_df = df[
        numerical_features
    ].reset_index(drop=True)


    # --------------------------------------------------------
    # Combine numerical + encoded features
    # --------------------------------------------------------

    X_final = pd.concat(
        [
            numerical_df,
            encoded_df.reset_index(drop=True)
        ],
        axis=1
    )


    # --------------------------------------------------------
    # EXACT SAME ORDER AS TRAINING
    # --------------------------------------------------------

    X_final = X_final[
        model.feature_names_in_
    ]


    # --------------------------------------------------------
    # MODEL PREDICTION
    # --------------------------------------------------------

    probability = model.predict_proba(
        X_final
    )[0][1]


    probability = float(probability)


    # --------------------------------------------------------
    # RISK LEVEL
    # --------------------------------------------------------

    if probability >= 0.50:

        risk = "High"

    elif probability >= 0.30:

        risk = "Medium"

    else:

        risk = "Low"


    # --------------------------------------------------------
    # EXPLAINABILITY
    # --------------------------------------------------------

    drivers = get_risk_drivers(
        employee
    )


    # --------------------------------------------------------
    # HR RECOMMENDATIONS
    # --------------------------------------------------------

    recommendations = get_recommendations(
        risk,
        drivers
    )


    # --------------------------------------------------------
    # FINAL RESPONSE
    # --------------------------------------------------------

    return {

        "attrition_probability": round(
            probability,
            3
        ),

        "risk_level": risk,

        "risk_drivers": drivers,

        "recommendations": recommendations
    }