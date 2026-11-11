# 💳 Fraud Detection System

An end-to-end Machine Learning project designed to identify potentially fraudulent financial transactions using classification algorithms. The project covers data analysis, model development, API development, Docker containerization, and AWS deployment.

## 🎯 Project Objectives

- Identify fraudulent financial transactions.
- Minimize false positives while improving fraud detection.
- Compare multiple Machine Learning algorithms.
- Develop an API that accepts transaction details and returns predictions.

## 📊 Data Analysis & Preprocessing

- Performed Exploratory Data Analysis (EDA) to understand transaction patterns.
- Handled missing values and encoded categorical variables.
- Applied sampling techniques to address class imbalance.
- Performed feature scaling where required.
- Analysed features associated with fraudulent transactions.

## 🤖 Machine Learning Models

Implemented and compared:

- Logistic Regression
- Random Forest Classifier
- Gradient Boosting
- XGBoost

Models were evaluated using Accuracy, Precision, Recall, F1-score, ROC-AUC, and Confusion Matrix.

## 🚀 Deployment

The trained model was integrated with a FastAPI backend and deployed on AWS using Docker.

- **FastAPI:** Developed REST API endpoints to receive transaction details and return fraud predictions.
- **Docker:** Containerized the application and its dependencies.
- **AWS:** Deployed the Dockerized FastAPI application on an AWS server.
- **Streamlit:** Developed an interactive frontend. Integration with the AWS-hosted API is currently in progress.

## 🔗 Live API

**FastAPI Swagger Documentation:**

[Fraud Detection API](http://16.171.255.195:8001/docs)

The API can be explored and tested through its Swagger documentation.

## 🛠️ Technologies Used

- **Programming:** Python
- **Data Analysis:** Pandas, NumPy, Matplotlib, Seaborn
- **Machine Learning:** Scikit-learn, XGBoost
- **Backend:** FastAPI
- **Frontend:** Streamlit (integration in progress)
- **Containerization:** Docker
- **Cloud Deployment:** AWS
- **Development:** Jupyter Notebook, VS Code

## 💡 Key Takeaways

- Experience in handling imbalanced financial datasets.
- Comparison of multiple Machine Learning classification algorithms.
- Integration of ML models with REST APIs.
- Practical experience in Docker containerization and AWS deployment.
- Understanding the process of developing and deploying an ML-based application.
