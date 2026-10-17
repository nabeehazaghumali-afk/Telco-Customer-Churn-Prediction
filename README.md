# 📊 Telco Customer Churn Prediction & Retention Analytics

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Scikit-Learn](https://img.shields.io/badge/Library-Scikit--Learn-orange.svg)
![Pandas](https://img.shields.io/badge/Data-Pandas%20%7C%20NumPy-green.svg)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen.svg)

## 🎯 Executive Summary
Customer churn is a critical metric for telecommunications companies. Acquiring new customers can cost up to 5 times more than retaining existing ones. This project builds an end-to-end Machine Learning pipeline using **Random Forest** to accurately predict customer churn and uncover key operational drivers, enabling business stakeholders to implement targeted retention strategies.

---

## 💡 Key Business Insights
- **Contract Type Dynamics**: Month-to-month contract holders show significantly higher churn compared to customers on 1-year or 2-year contracts.
- **Tenure & Monthly Charges**: High monthly charges combined with low tenure (< 12 months) form the primary risk zone for churn.
- **Service Features**: Customers without online security or tech support services are more prone to leaving.

---

## 🛠️ Project Architecture & Methodology

1. **Data Preprocessing & Cleaning**:
   - Handled missing and whitespace values in `TotalCharges`.
   - Converted data types and removed non-informative identifiers (`customerID`).

2. **Feature Engineering & Encoding**:
   - Mapped binary target variable `Churn` (1 for Yes, 0 for No).
   - Applied One-Hot Encoding (`pd.get_dummies`) to categorical independent features.

3. **Model Development & Class Imbalance Handling**:
   - Split dataset into 80% Training and 20% Testing sets using stratified sampling.
   - Employed `RandomForestClassifier` with `class_weight='balanced'` to compensate for target variable imbalance.

4. **Model Evaluation & Interpretation**:
   - Evaluated model using Accuracy, Precision, Recall, and F1-Score.
   - Extracted and visualized Top 10 Feature Importances for business actionability.

---

## 📈 Model Performance & Feature Importance

- **Accuracy**: ~79%
- **Recall (Class 1 - Churn)**: Optimized with balanced class weighting to capture high-risk customers effectively.

### Top Drivers of Churn:
1. `TotalCharges`
2. `tenure`
3. `MonthlyCharges`
4. `Contract_Two year`
5. `PaymentMethod_Electronic check`

---

## 💡 Strategic Recommendations for Retention
- **Incentivize Long-Term Contracts**: Offer small discounts or value-added upgrades to transition month-to-month customers to annual contracts.
- **Early-Stage Engagement**: Focus customer success efforts on new users during their first 6–12 months.
- **Bundle Support Services**: Promote free trials for Security and Tech Support features during onboarding to increase product stickiness.
