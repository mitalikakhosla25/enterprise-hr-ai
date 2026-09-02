import { useState } from "react";
import "./App.css";

const API_URL = "http://127.0.0.1:8000";

function EmployeeRisk() {
  const [employee, setEmployee] = useState({
    Age: 35,
    BusinessTravel: "Travel_Rarely",
    DailyRate: 800,
    Department: "Research & Development",
    DistanceFromHome: 10,
    Education: 3,
    EducationField: "Life Sciences",
    EmployeeCount: 1,
    EmployeeNumber: 1001,
    EnvironmentSatisfaction: 3,
    Gender: "Male",
    HourlyRate: 70,
    JobInvolvement: 3,
    JobLevel: 2,
    JobRole: "Research Scientist",
    JobSatisfaction: 3,
    MaritalStatus: "Single",
    MonthlyIncome: 5000,
    MonthlyRate: 14000,
    NumCompaniesWorked: 2,
    Over18: "Y",
    OverTime: "No",
    PercentSalaryHike: 15,
    PerformanceRating: 3,
    RelationshipSatisfaction: 3,
    StandardHours: 80,
    StockOptionLevel: 0,
    TotalWorkingYears: 8,
    TrainingTimesLastYear: 3,
    WorkLifeBalance: 3,
    YearsAtCompany: 5,
    YearsInCurrentRole: 3,
    YearsSinceLastPromotion: 1,
    YearsWithCurrManager: 3,
  });

  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const handleChange = (e) => {
    const { name, value } = e.target;

    const numericFields = [
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
    ];

    setEmployee((prev) => ({
      ...prev,
      [name]: numericFields.includes(name) ? Number(value) : value,
    }));

    // Clear old prediction when employee information changes
    setResult(null);
  };

  const predictRisk = async () => {
    setLoading(true);
    setError("");
    setResult(null);

    try {
      const response = await fetch(`${API_URL}/predict/attrition`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(employee),
      });

      if (!response.ok) {
        throw new Error(`Server returned ${response.status}`);
      }

      const data = await response.json();

      setResult(data);
    } catch (err) {
      console.error(err);

      setError(
        "Unable to connect to the HR AI backend. Make sure FastAPI is running on port 8000."
      );
    } finally {
      setLoading(false);
    }
  };

  const getRiskColor = () => {
    if (!result) return "";

    if (result.risk_level === "High") {
      return "risk-high";
    }

    if (result.risk_level === "Medium") {
      return "risk-medium";
    }

    return "risk-low";
  };

  return (
    <div className="risk-page">

      {/* ================= HEADER ================= */}

      <div className="risk-header">
        <div>
          <div className="ai-status">
            <span className="ai-status-dot"></span>
            AI MODEL ONLINE
          </div>

          <h1>Employee Risk Assessment</h1>

          <p>
            Analyze employee profiles and identify potential attrition risk
            using the Enterprise HR AI model.
          </p>
        </div>
      </div>


      {/* ================= MAIN LAYOUT ================= */}

      <div className="risk-layout">

        {/* ================= EMPLOYEE FORM ================= */}

        <div className="risk-card">

          <div className="section-heading">
            <div>
              <h2>Employee Information</h2>

              <p>
                Enter the employee profile to generate an AI risk assessment.
              </p>
            </div>
          </div>


          <div className="form-grid">

            {/* Employee Number */}

            <div className="form-group">
              <label>Employee Number</label>

              <input
                type="number"
                name="EmployeeNumber"
                value={employee.EmployeeNumber}
                onChange={handleChange}
              />
            </div>


            {/* Age */}

            <div className="form-group">
              <label>Age</label>

              <input
                type="number"
                name="Age"
                min="18"
                max="70"
                value={employee.Age}
                onChange={handleChange}
              />
            </div>


            {/* Department */}

            <div className="form-group">
              <label>Department</label>

              <select
                name="Department"
                value={employee.Department}
                onChange={handleChange}
              >
                <option value="Research & Development">
                  Research & Development
                </option>

                <option value="Sales">
                  Sales
                </option>

                <option value="Human Resources">
                  Human Resources
                </option>
              </select>
            </div>


            {/* Job Role */}

            <div className="form-group">
              <label>Job Role</label>

              <select
                name="JobRole"
                value={employee.JobRole}
                onChange={handleChange}
              >
                <option value="Research Scientist">
                  Research Scientist
                </option>

                <option value="Laboratory Technician">
                  Laboratory Technician
                </option>

                <option value="Sales Executive">
                  Sales Executive
                </option>

                <option value="Sales Representative">
                  Sales Representative
                </option>

                <option value="Manager">
                  Manager
                </option>

                <option value="Healthcare Representative">
                  Healthcare Representative
                </option>

                <option value="Human Resources">
                  Human Resources
                </option>

                <option value="Manufacturing Director">
                  Manufacturing Director
                </option>

                <option value="Research Director">
                  Research Director
                </option>
              </select>
            </div>


            {/* Monthly Income */}

            <div className="form-group">
              <label>Monthly Income</label>

              <input
                type="number"
                name="MonthlyIncome"
                min="0"
                value={employee.MonthlyIncome}
                onChange={handleChange}
              />
            </div>


            {/* Overtime */}

            <div className="form-group">
              <label>Overtime</label>

              <select
                name="OverTime"
                value={employee.OverTime}
                onChange={handleChange}
              >
                <option value="No">No</option>
                <option value="Yes">Yes</option>
              </select>
            </div>


            {/* Job Satisfaction */}

            <div className="form-group">
              <label>Job Satisfaction</label>

              <select
                name="JobSatisfaction"
                value={employee.JobSatisfaction}
                onChange={handleChange}
              >
                <option value="1">1 - Low</option>
                <option value="2">2 - Medium</option>
                <option value="3">3 - High</option>
                <option value="4">4 - Very High</option>
              </select>
            </div>


            {/* Work Life Balance */}

            <div className="form-group">
              <label>Work-Life Balance</label>

              <select
                name="WorkLifeBalance"
                value={employee.WorkLifeBalance}
                onChange={handleChange}
              >
                <option value="1">1 - Bad</option>
                <option value="2">2 - Good</option>
                <option value="3">3 - Better</option>
                <option value="4">4 - Best</option>
              </select>
            </div>


            {/* Business Travel */}

            <div className="form-group">
              <label>Business Travel</label>

              <select
                name="BusinessTravel"
                value={employee.BusinessTravel}
                onChange={handleChange}
              >
                <option value="Travel_Rarely">
                  Travel Rarely
                </option>

                <option value="Travel_Frequently">
                  Travel Frequently
                </option>

                <option value="Non-Travel">
                  Non-Travel
                </option>
              </select>
            </div>


            {/* Gender */}

            <div className="form-group">
              <label>Gender</label>

              <select
                name="Gender"
                value={employee.Gender}
                onChange={handleChange}
              >
                <option value="Male">Male</option>
                <option value="Female">Female</option>
              </select>
            </div>


            {/* Marital Status */}

            <div className="form-group">
              <label>Marital Status</label>

              <select
                name="MaritalStatus"
                value={employee.MaritalStatus}
                onChange={handleChange}
              >
                <option value="Single">Single</option>
                <option value="Married">Married</option>
                <option value="Divorced">Divorced</option>
              </select>
            </div>


            {/* Education */}

            <div className="form-group">
              <label>Education Level</label>

              <select
                name="Education"
                value={employee.Education}
                onChange={handleChange}
              >
                <option value="1">1</option>
                <option value="2">2</option>
                <option value="3">3</option>
                <option value="4">4</option>
                <option value="5">5</option>
              </select>
            </div>

          </div>


          {/* ================= BUTTON ================= */}

          <button
            className="predict-button"
            onClick={predictRisk}
            disabled={loading}
          >
            {loading ? (
              <>
                <span className="button-spinner"></span>
                Analyzing Employee...
              </>
            ) : (
              "Predict Attrition Risk"
            )}
          </button>


          {/* ================= ERROR ================= */}

          {error && (
            <div className="error-box">
              <strong>Prediction Error</strong>

              <p>{error}</p>
            </div>
          )}

        </div>


        {/* ================= RESULT CARD ================= */}

        <div className="risk-card result-card">

          <h2>AI Risk Assessment</h2>


          {/* Empty State */}

          {!result && !loading && !error && (
            <div className="empty-result">

              <div className="empty-icon">
                AI
              </div>

              <h3>Ready to Analyze</h3>

              <p>
                Enter the employee information and click{" "}
                <strong>Predict Attrition Risk</strong> to generate an
                AI-powered assessment.
              </p>

            </div>
          )}


          {/* Loading State */}

          {loading && (
            <div className="empty-result">

              <div className="loading-spinner"></div>

              <h3>Analyzing Employee</h3>

              <p>
                The AI model is analyzing the employee profile...
              </p>

            </div>
          )}


          {/* Prediction Result */}

{result && (
  <div className="prediction-result">

    {/* Probability */}

    <div className="probability">

      <span>
        ATTRITION PROBABILITY
      </span>

      <strong>
        {(result.attrition_probability * 100).toFixed(1)}%
      </strong>

    </div>


    {/* Risk Badge */}

    <div className={`risk-badge ${getRiskColor()}`}>
      {result.risk_level} Risk
    </div>


    {/* Risk Message */}

    <div className="result-message">

      {result.risk_level === "High" && (
        <>
          <h3>
            ⚠ Immediate Attention Recommended
          </h3>

          <p>
            This employee shows a high predicted likelihood
            of attrition.
          </p>
        </>
      )}

      {result.risk_level === "Medium" && (
        <>
          <h3>
            ◐ Monitor Employee
          </h3>

          <p>
            This employee has a moderate predicted attrition risk.
          </p>
        </>
      )}

      {result.risk_level === "Low" && (
        <>
          <h3>
            ✓ Low Attrition Risk
          </h3>

          <p>
            The current employee profile indicates a relatively
            low predicted likelihood of attrition.
          </p>
        </>
      )}

    </div>


    {/* ================= RISK DRIVERS ================= */}

    {result.risk_drivers &&
      result.risk_drivers.length > 0 && (

      <div className="risk-drivers">

        <div className="analysis-title">
          <h3>Risk Drivers</h3>

          <span>
            Why the model may be flagging this employee
          </span>
        </div>


        {result.risk_drivers.map((driver, index) => (

          <div
            className="driver-card"
            key={index}
          >

            <div className="driver-top">

              <strong>
                {driver.factor}
              </strong>

              <span
                className={`impact-${driver.impact.toLowerCase()}`}
              >
                {driver.impact}
              </span>

            </div>

            <p>
              {driver.reason}
            </p>

          </div>

        ))}

      </div>

    )}


    {/* ================= RECOMMENDATIONS ================= */}

    {result.recommendations &&
      result.recommendations.length > 0 && (

      <div className="recommendations">

        <div className="analysis-title">

          <h3>
            Recommended HR Actions
          </h3>

          <span>
            Suggested next steps
          </span>

        </div>


        {result.recommendations.map(
          (recommendation, index) => (

          <div
            className="recommendation-item"
            key={index}
          >

            <span className="recommendation-number">
              {index + 1}
            </span>

            <p>
              {recommendation}
            </p>

          </div>

        ))}

      </div>

    )}

  </div>
)}

        </div>

      </div>
    </div>
  );
}

export default EmployeeRisk;