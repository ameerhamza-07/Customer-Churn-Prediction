

## 📌 Project Overview

This project is an end-to-end Customer Churn Prediction System that helps telecom companies identify customers who are likely to leave their services. The project integrates PostgreSQL, Machine Learning, Power BI, and Streamlit to provide data analysis, predictive modeling, and an interactive web application.

## 🚀 Features

* Data preprocessing and cleaning
* PostgreSQL database integration
* SQL-based business analysis
* Exploratory Data Analysis (EDA)
* Machine Learning model comparison
* Logistic Regression model deployment
* Interactive Streamlit web application
* Power BI dashboard for business insights
* Customer churn probability prediction
* Risk categorization (Low, Medium, High)


## 🛠️ Technology Stack

* Python
* Pandas
* NumPy
* Scikit-learn
* XGBoost
* PostgreSQL
* SQLAlchemy
* Power BI
* Streamlit
* Joblib
* Matplotlib
* Seaborn

## 📂 Project Structure

Customer-Churn-Prediction/
│
├── app.py
├── Customer_Churn_Prediction.ipynb
├── customer_churn_pipeline.pkl
├── Telco_customer_churn.xlsx
├── requirements.txt
├── README.md
|
├── dashboard/
│   └── Customer_Churn_Dashboard.pbix
│
├── sql/
│   └── analysis_queries.sql
│
├── screenshots/
│   ├── dashboard.png
│   ├── streamlit_home.png
│   ├── prediction.png
│   └── database.png
│
└── images/
    └── architecture.png

## 🗄️ Database

The dataset is imported into PostgreSQL , where SQL queries are used to perform customer analysis and generate business insights.

Examples include:

* Total Customers
* Churn Rate
* Contract Analysis
* Internet Service Analysis
* Revenue Analysis
* Customer Lifetime Value (CLTV)


## 🤖 Machine Learning

The following machine learning models were trained and compared:

* Logistic Regression
* Decision Tree
* Random Forest
* XGBoost

After evaluating the models using Accuracy, Precision, Recall, and F1-Score, **Logistic Regression** was selected as the final model.

The complete preprocessing pipeline and trained model were saved as:

customer_churn_pipeline.pkl


## 🌐 Streamlit Web Application

The Streamlit application allows users to:

* Enter customer information
* Predict customer churn
* View churn probability
* Display customer risk level
* View entered customer details

Run the application using:

```bash
streamlit run app.py
```

---

## 📈 Power BI Dashboard

The interactive dashboard includes:

* Total Customers
* Churn Rate
* Total Revenue
* Average CLTV
* Contract-wise Churn
* Internet Service Analysis
* Payment Method Analysis
* Revenue Segment Analysis
* Customer Distribution by State

---

## 📊 Model Workflow

```
Excel Dataset
      │
      ▼
PostgreSQL Database
      │
      ▼
Jupyter Notebook
(Data Cleaning + SQL Analysis + EDA)
      │
      ▼
Machine Learning
(Logistic Regression, Decision Tree,
Random Forest, XGBoost)
      │
      ▼
Best Model Selection
      │
      ▼
customer_churn_pipeline.pkl
      │
      ▼
Streamlit Application
      │
      ▼
Customer Churn Prediction
```

---


## 📌 Future Improvements

* Hyperparameter tuning
* Cross-validation
* Cloud deployment
* Docker containerization
* User authentication
* Automated model retraining
* Real-time prediction API

---

