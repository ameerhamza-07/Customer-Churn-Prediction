

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

## 🏗️ Project Architecture

The Customer Churn Prediction System follows an end-to-end data analytics and machine learning workflow.

             Customer Churn Prediction System

        ┌────────────────────────────────────────────┐
        │        Telco_customer_churn.xlsx           │
        │             (Dataset Source)               │
        └────────────────────────────────────────────┘
                            │
                            ▼
        ┌────────────────────────────────────────────┐
        │         PostgreSQL Database                │
        │     Data Storage & SQL Analysis            │
        └────────────────────────────────────────────┘
                            │
                            ▼
        ┌────────────────────────────────────────────┐
        │          Jupyter Notebook                  │
        │ • Data Cleaning                            │
        │ • Exploratory Data Analysis                │
        │ • Feature Engineering                      │
        │ • SQL Integration                          │
        └────────────────────────────────────────────┘
                            │
                            ▼
        ┌────────────────────────────────────────────┐
        │       Machine Learning Models              │
        │ • Logistic Regression                      │
        │ • Decision Tree                            │
        │ • Random Forest                            │
        │ • XGBoost                                  │
        └────────────────────────────────────────────┘
                            │
                            ▼
        ┌────────────────────────────────────────────┐
        │     Best Model Selected                    │
        │   Logistic Regression Pipeline             │
        │ customer_churn_pipeline.pkl                │
        └────────────────────────────────────────────┘
                            │
              ┌─────────────┴─────────────┐
              ▼                           ▼
┌──────────────────────────────┐   ┌──────────────────────────┐
│     Streamlit Web App        │   │     Power BI Dashboard   │
│ • Customer Input             │   │ • KPI Cards              │
│ • Churn Prediction           │   │ • Churn Analysis         │
│ • Churn Probability          │   │ • Revenue Analysis       │
│ • Risk Category              │   │ • CLTV Analysis          │
└──────────────────────────────┘   └──────────────────────────┘

### Workflow Description

1. **Dataset Collection**

   * The project begins with the **Telco Customer Churn** dataset stored in an Excel file.

2. **Database Integration**

   * The dataset is imported into **PostgreSQL** for efficient storage and SQL-based analysis.

3. **Data Processing**

   * Data cleaning, preprocessing, missing value handling, feature engineering, and exploratory data analysis (EDA) are performed using **Python** and **Jupyter Notebook**.

4. **Machine Learning**

   * Multiple machine learning algorithms are trained and evaluated:

     * Logistic Regression
     * Decision Tree
     * Random Forest
     * XGBoost

5. **Model Selection**

   * Based on model evaluation metrics (Accuracy, Precision, Recall, and F1-Score), **Logistic Regression** is selected as the final model.
   * The complete preprocessing pipeline and trained model are saved as `customer_churn_pipeline.pkl`.

6. **Streamlit Deployment**

   * The trained pipeline is deployed as an interactive Streamlit web application.
   * Users can enter customer details to obtain:

     * Churn prediction
     * Churn probability
     * Risk category (Low, Medium, High)

7. **Business Intelligence Dashboard**

   * Power BI connects to the PostgreSQL database to create interactive dashboards that visualize:

     * Customer distribution
     * Churn rate
     * Contract-wise churn
     * Internet service analysis
     * Payment method analysis
     * Revenue segmentation
     * Customer Lifetime Value (CLTV)
     * Geographic customer distribution

---

## 📈 Model Performance
| Model | Accuracy | Precision | Recall | F1 Score | ROC AUC |
| Logistic Regression| 79.99% |64.38% |55.08% | 59.37% |84.88%|
| Random Forest      | 78.64% | 62.21% | 49.73% | 55.27% | 83.98% |
| XGBoost            | 79.28% | 62.65% | 54.28% | 58.17% | 83.45% |
| Decision Tree      | 71.82% | 47.06% | 49.20% | 48.10% | 64.60% |

Final Selected Model:Logistic Regression

## 🎯 Business Objective

The primary objective of this project is to help telecom companies identify customers who are likely to churn. By predicting churn probability in advance, businesses can implement targeted retention strategies, reduce customer loss, improve customer satisfaction, and increase overall revenue.


