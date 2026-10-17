import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Telco Churn AI Dashboard", layout="wide")

st.title("📊 Telco Customer Churn Prediction Dashboard")
st.write("An Interactive ML Web App for Real-Time Churn Risk Assessment")

# Sidebar inputs
st.sidebar.header("Customer Profile Parameters")
tenure = st.sidebar.slider("Tenure (Months)", 0, 72, 12)
monthly_charges = st.sidebar.slider("Monthly Charges ($)", 18.0, 120.0, 70.0)
contract = st.sidebar.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"])
tech_support = st.sidebar.checkbox("Tech Support Enabled")

# Prediction logic simulation
churn_prob = 0.5
if tenure < 12 and contract == "Month-to-month":
    churn_prob += 0.3
if contract == "Two year":
    churn_prob -= 0.3

churn_prob = max(0.05, min(0.95, churn_prob))

st.subheader("Model Prediction Output")
col1, col2 = st.columns(2)
col1.metric("Predicted Churn Probability", f"{churn_prob*100:.1f}%")

if churn_prob > 0.5:
    col2.error("High Risk Customer! Immediate Retention Strategy Required.")
else:
    col2.success("Low Risk Customer! Stable Engagement.")
