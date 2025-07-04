#  Customer Churn Prediction using Machine Learning

##  Objective
This project aims to build a machine learning model that predicts whether a customer is likely to churn based on service usage, contract type, and demographic data. It helps telecom businesses proactively engage high-risk customers and minimize churn-related losses.

##  Dataset
- **Source**: IBM Watson Telco Customer Churn dataset
- **URL**: [Telco Dataset - GitHub](https://github.com/IBM/telco-customer-churn-on-icp4d/blob/master/data/Telco-Customer-Churn.csv)
- **Records**: 7043 rows, 21 features

##  Tech Stack
- Python (Pandas, NumPy, Matplotlib, Seaborn)
- Scikit-learn
- XGBoost
- SHAP (Explainability)
- Jupyter Notebook

##  ML Pipeline
1. Load & clean data
2. Handle categorical variables using One-Hot Encoding
3. Split dataset into training and testing sets
4. Train `XGBoostClassifier`
5. Evaluate performance using classification metrics
6. Use SHAP to interpret top features
7. Estimate revenue saved from retaining predicted churners

##  Results
- **Accuracy**: 76%
- **Precision (Churn)**: 57%
- **Recall (Churn)**: 47%
- **F1-score (Churn)**: 51%
- **ROC-AUC Score**: ~0.83 (visualized using SHAP)

##  Key Features Driving Churn
(from SHAP summary plot):
- Low Tenure
- Contract Type (Month-to-Month)
- High Monthly Charges
- Absence of Tech Support
- Fiber Optic Internet & Online Security status

##  Business Impact
- Predicted high-risk churners and estimated business loss if not retained.
- **Estimated Monthly Revenue Saved** if at-risk customers are retained: **₹12830.05**

