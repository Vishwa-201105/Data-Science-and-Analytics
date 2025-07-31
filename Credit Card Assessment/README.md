#  Credit Card Fraud Detection

##  Project Overview

This project focuses on detecting fraudulent transactions from anonymized credit card data using machine learning. The dataset is highly imbalanced, and special techniques like **SMOTE** and **class weighting** are applied to improve model performance. The goal is to build a reliable and interpretable model to classify transactions as legitimate or fraudulent.

---

##  Objectives

- Explore and understand transaction patterns in the dataset.
- Address severe class imbalance using oversampling and model-level adjustments.
- Build and evaluate a machine learning model using appropriate metrics for fraud detection.
- Present results using insightful visualizations and performance reports.

---

##  Dataset

- **Source**: [Kaggle - Credit Card Fraud Detection](https://www.kaggle.com/mlg-ulb/creditcardfraud)
- **Features**:
  - `V1` to `V28`: Result of PCA transformation (feature confidentiality preserved)
  - `Amount`: Transaction amount
  - `Time`: Seconds elapsed between transaction and first transaction
  - `Class`: Target variable (0 = Not Fraud, 1 = Fraud)
- **Imbalance**: Highly imbalanced data with <1% fraudulent transactions

---

## 🛠 Technologies Used

- **Languages & Libraries**: Python, pandas, NumPy, scikit-learn, seaborn, matplotlib, imbalanced-learn
- **Key Techniques**: Data preprocessing, feature scaling, SMOTE oversampling, Random Forest modeling

---

##  Exploratory Data Analysis

- Inspected class distribution (`Class` column) and confirmed heavy class imbalance.
- Visualized:
  - Distribution of transaction `Amount`
  - Correlation matrix using heatmap
- Decided to drop `Time` feature due to low relevance.

---

##  Modeling Approach

1. **Preprocessing**:
   - Scaled `Amount` feature using `StandardScaler`
   - Dropped `Time` feature
2. **Train-Test Split**:
   - Performed stratified 70:30 split to maintain class ratio
3. **Handling Imbalance**:
   - Applied **SMOTE** to training set to balance minority class
   - Also tried `class_weight='balanced'` in Random Forest
4. **Modeling**:
   - Used `RandomForestClassifier` with 100 trees
   - Trained on both original and SMOTE-balanced data
5. **Evaluation**:
   - Confusion matrix
   - Classification report (Precision, Recall, F1-score)
   - ROC-AUC score
   - Precision-Recall curve

---

##  Results

- **High precision and recall** for the minority (fraudulent) class using both SMOTE and class weighting
- **ROC-AUC** and **PR curves** demonstrated strong performance in identifying fraudulent cases
- Learned importance of choosing proper metrics for imbalanced datasets (accuracy is misleading)

---

##  Key Learnings

- Effective use of SMOTE and `class_weight` to handle imbalance
- Importance of business-aligned metrics like Precision and Recall in fraud detection
- Feature scaling and visualization play crucial roles in pipeline setup
- Evaluation beyond accuracy is vital in real-world applications like finance and banking

---


