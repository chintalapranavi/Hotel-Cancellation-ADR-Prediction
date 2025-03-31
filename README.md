# 🏨 Hotel Booking Cancellation & ADR Prediction

This project aims to optimize revenue management for hotels by predicting booking cancellations and forecasting Average Daily Rate (ADR) using machine learning and big data techniques. We leveraged distributed processing with Apache Spark and PySpark to handle large-scale hotel booking data (119,000+ records), and built predictive models to support dynamic pricing and operational efficiency.

## 📌 Problem Statement

High cancellation rates and fluctuating ADRs pose major challenges in the hospitality industry. This project tackles:
- Predicting whether a hotel booking will be cancelled
- Forecasting the ADR, a key financial metric

## 🔍 Key Objectives
- Identify major drivers of cancellations and ADR
- Build robust machine learning models for prediction
- Provide actionable insights for dynamic pricing and strategic planning

## 🚀 Tools & Technologies
- **Languages**: Python
- **Libraries**: Pandas, NumPy, Matplotlib, Seaborn, scikit-learn, TensorFlow, Keras, xgboost
- **Big Data Tools**: Apache Spark, PySpark
- **Data Engineering**: Data Cleaning, Feature Engineering, ETL, Outlier Detection
- **Visualization**: Tableau, matplotlib, Streamlit
- **DevOps**: Git, Docker, CI/CD
- **Modeling Techniques**: 
  - Classification: Logistic Regression, Decision Tree, Random Forest, SVM
  - Regression: Linear Regression, Generalized Linear Regression, Gradient Boosted Trees, Random Forest Regressor

## 🧠 Methodology

### Data Preprocessing & Cleaning
- Removed nulls, duplicates, and inconsistent rows
- Handled outliers using Z-scores
- Combined relevant columns (e.g., `babies` + `children` → `kids`)
- Extracted date parts and seasonality

### Feature Engineering
- One-hot encoding, string indexing, and MinMax scaling
- Chi-square selection for feature importance
- Correlation analysis and statistical tests

### Model Building
- Classification for Cancellation Prediction
  - Best Model: Random Forest (Accuracy: 99.96%)
- Regression for ADR Prediction
  - Best Model: Gradient Boosted Trees (RMSE: 37.37, R²: 0.42)

## 📊 Results & Impact
- Identified hotel type, lead time, and market segment as strong predictors
- Built models that can assist hotels with targeted marketing, dynamic pricing, and resource allocation
- Achieved high accuracy and interpretability across both tasks
- Delivered insights via dashboards and visual reports

## 🌐 Deployment
- Built an interactive Streamlit app to explore trends and predictions
- Containerized the workflow using Docker for reproducibility

## 📁 Dataset
- [Hotel Booking Demand Dataset (Kaggle)](https://www.kaggle.com/datasets/jessemostipak/hotel-booking-demand)

## 🙋‍♀️ Author
**Pranavi Chintala**  
Master's in Data Science, University at Buffalo  


---

Feel free to star ⭐ this repo or fork 🍴 it to explore more on hotel analytics and revenue optimization!
