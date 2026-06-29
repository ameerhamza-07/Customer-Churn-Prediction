import streamlit as st
import pandas as pd
from joblib import load

# ==========================
# Load Model
# ==========================
model = load("customer_churn_pipeline.pkl")

# ==========================
# Page Configuration
# ==========================
st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Customer Churn Prediction")
st.write("Predict whether a telecom customer is likely to churn.")

# ==========================
# Customer Information
# ==========================

col1, col2 = st.columns(2)

with col1:

    gender = st.selectbox(
        "Gender",
        ["Male", "Female"]
    )

    senior_citizen = st.selectbox(
        "Senior Citizen",
        ["Yes", "No"]
    )

    partner = st.selectbox(
        "Partner",
        ["Yes", "No"]
    )

    dependents = st.selectbox(
        "Dependents",
        ["Yes", "No"]
    )

    tenure_months = st.slider(
        "Tenure Months",
        0,
        72,
        12
    )

    phone_service = st.selectbox(
        "Phone Service",
        ["Yes", "No"]
    )

    multiple_lines = st.selectbox(
        "Multiple Lines",
        ["Yes", "No", "No phone service"]
    )

    internet_service = st.selectbox(
        "Internet Service",
        ["DSL", "Fiber optic", "No"]
    )

    online_security = st.selectbox(
        "Online Security",
        ["Yes", "No", "No internet service"]
    )

    online_backup = st.selectbox(
        "Online Backup",
        ["Yes", "No", "No internet service"]
    )

with col2:

    device_protection = st.selectbox(
        "Device Protection",
        ["Yes", "No", "No internet service"]
    )

    tech_support = st.selectbox(
        "Tech Support",
        ["Yes", "No", "No internet service"]
    )

    streaming_tv = st.selectbox(
        "Streaming TV",
        ["Yes", "No", "No internet service"]
    )

    streaming_movies = st.selectbox(
        "Streaming Movies",
        ["Yes", "No", "No internet service"]
    )

    contract = st.selectbox(
        "Contract",
        [
            "Month-to-month",
            "One year",
            "Two year"
        ]
    )

    paperless_billing = st.selectbox(
        "Paperless Billing",
        ["Yes", "No"]
    )

    payment_method = st.selectbox(
        "Payment Method",
        [
            "Electronic check",
            "Mailed check",
            "Bank transfer (automatic)",
            "Credit card (automatic)"
        ]
    )

    monthly_charges = st.number_input(
        "Monthly Charges",
        min_value=0.0,
        max_value=200.0,
        value=70.0
    )

    total_charges = st.number_input(
        "Total Charges",
        min_value=0.0,
        max_value=10000.0,
        value=1000.0
    )

    cltv = st.number_input(
        "CLTV",
        min_value=0,
        max_value=10000,
        value=4500
    )

    revenue_segment = st.selectbox(
        "Revenue Segment",
        [
            "Low",
            "Medium",
            "High"
        ]
    )

    tenure_group = st.selectbox(
        "Tenure Group",
        [
            "0-12 Months",
            "13-24 Months",
            "25-48 Months",
            "49-72 Months"
        ]
    )

# ==========================
# Prediction
# ==========================

if st.button("Predict Churn"):

    input_df = pd.DataFrame({

        "gender": [gender],
        "senior_citizen": [senior_citizen],
        "partner": [partner],
        "dependents": [dependents],
        "tenure_months": [tenure_months],
        "phone_service": [phone_service],
        "multiple_lines": [multiple_lines],
        "internet_service": [internet_service],
        "online_security": [online_security],
        "online_backup": [online_backup],
        "device_protection": [device_protection],
        "tech_support": [tech_support],
        "streaming_tv": [streaming_tv],
        "streaming_movies": [streaming_movies],
        "contract": [contract],
        "paperless_billing": [paperless_billing],
        "payment_method": [payment_method],
        "monthly_charges": [monthly_charges],
        "total_charges": [total_charges],
        "cltv": [cltv],
        "revenue_segment": [revenue_segment],
        "tenure_group": [tenure_group]

    })

    prediction = model.predict(input_df)[0]

    probability = model.predict_proba(input_df)[0][1]

    st.metric(
        label="Churn Probability",
        value=f"{probability:.2%}"
    )

    if prediction == 1:

        st.error(
            f"⚠️ Customer is likely to churn\n\nProbability: {probability:.2%}"
        )

    else:

        st.success(
            f"✅ Customer is likely to stay\n\nProbability: {(1-probability):.2%}"
        )

    st.subheader("Risk Level")

    if probability < 0.30:

        st.success("🟢 Low Risk")

    elif probability < 0.70:

        st.warning("🟡 Medium Risk")

    else:

        st.error("🔴 High Risk")

    st.subheader("Customer Information")

    st.dataframe(
        input_df,
        use_container_width=True
    )