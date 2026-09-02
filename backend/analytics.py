from .data_loader import hr_data


def dashboard_summary():

    total = len(hr_data)

    active = (
        hr_data["EmployeeStatus"] == "Active"
    ).sum()

    terminated = (
        hr_data["EmployeeStatus"].isin([
            "Voluntarily Terminated",
            "Terminated for Cause"
        ])
    ).sum()

    attrition_rate = (
        terminated / total * 100
        if total > 0 else 0
    )

    return {
        "total_employees": int(total),
        "active_employees": int(active),
        "terminated_employees": int(terminated),
        "attrition_rate": round(float(attrition_rate), 2),
        "average_engagement": round(
            float(hr_data["Engagement Score"].mean()), 2
        ),
        "average_satisfaction": round(
            float(hr_data["Satisfaction Score"].mean()), 2
        ),
        "average_work_life_balance": round(
            float(hr_data["Work-Life Balance Score"].mean()), 2
        )
    }


def department_analysis():

    result = (
        hr_data.groupby("DepartmentType")
        .agg(
            employees=("Employee ID", "count"),
            avg_engagement=("Engagement Score", "mean"),
            avg_satisfaction=("Satisfaction Score", "mean"),
            avg_performance=("Current Employee Rating", "mean")
        )
        .round(2)
        .reset_index()
    )

    return result.to_dict(orient="records")


def performance_analysis():

    result = (
        hr_data["Performance Score"]
        .value_counts()
        .reset_index()
    )

    result.columns = ["performance", "employees"]

    return result.to_dict(orient="records")


def training_analysis():

    result = (
        hr_data["Training Outcome"]
        .value_counts()
        .reset_index()
    )

    result.columns = ["outcome", "employees"]

    return result.to_dict(orient="records")

def get_employees():

    columns = [
        "Employee ID",
        "First Name",
        "Last Name",
        "DepartmentType",
        "Position",
        "EmployeeStatus"
    ]

    available_columns = [
        column for column in columns
        if column in hr_data.columns
    ]

    employees = hr_data[available_columns].copy()

    return employees.to_dict(orient="records")