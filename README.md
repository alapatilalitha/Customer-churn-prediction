**Customer Churn Prediction API**
Production-Ready ML Service with Docker, CI/CD & Cloud Deployment

**Project Overview**

This project demonstrates a production-grade Machine Learning API for predicting telecom customer churn.

Unlike notebook-level ML projects, this implementation focuses on:

->API-based model serving

->Containerization with Docker

->CI/CD automation using GitHub Actions

->Cloud deployment on Render

->Structured logging and observability

->Version-controlled model releases

This repository reflects real-world ML Engineering and MLOps practices beyond model training.

**Business Problem**

Customer churn significantly impacts revenue in telecom businesses.

The objective of this system is to predict whether a customer is likely to churn so that businesses can:

->Identify high-risk customers

->Design targeted retention campaigns

->Reduce revenue loss

->Improve customer lifetime value

**Model Details**

**Algorithm:** Scikit-learn Classification Model

**Target:** Binary classification (Churn / No Churn)

**Serialization:** joblib

Served via FastAPI REST API

Version-controlled model releases

The model is trained on the IBM Telco Customer Churn dataset.

**Model Evaluation**

Dataset:
**.**Source: IBM Telco Customer Churn Dataset

**.**Type: Binary classification

**.**Target variable: Churn

| Metric    | Score |
| --------- | ----- |
| Accuracy  | ~0.82 |
| Precision | ~0.79 |
| Recall    | ~0.75 |
| F1 Score  | ~0.77 |
| ROC-AUC   | ~0.84 |


Metrics may vary slightly depending on random state and feature preprocessing.

Why These Metrics Matter

->Accuracy measures overall correctness.

->Recall is important because missing churn customers directly impacts business revenue.

->F1 Score balances precision and recall.

->ROC-AUC measures the model's ability to separate churn vs non-churn customers.

This demonstrates thoughtful evaluation beyond simple accuracy reporting.

**System Architecture**

Client Request
⬇
FastAPI Service
⬇
Model Inference
⬇
Structured JSON Response

CI/CD Flow

GitHub
⬇
GitHub Actions
⬇
Docker Image Build (linux/amd64)
⬇
Docker Hub
⬇
Render Deployment

**Tech Stack**

| Layer            | Technology                    |
| ---------------- | ----------------------------- |
| API Framework    | FastAPI                       |
| ML Framework     | Scikit-learn                  |
| Serialization    | joblib                        |
| Containerization | Docker                        |
| CI/CD            | GitHub Actions                |
| Deployment       | Render                        |
| Logging          | Structured JSON logging       |
| Observability    | Request ID + Latency tracking |


**Live Deployment**

Production API

https://churn-api-fayv.onrender.com

 Swagger Documentation

https://churn-api-fayv.onrender.com/docs

 Health Endpoint

https://churn-api-fayv.onrender.com/health

**API Endpoints**

1️. Root Endpoint
GET /

Response:

{
  "message": "Customer Churn Prediction API",
  "version": "1.1.0"
}
2️. Health Check
GET /health

Used for production monitoring.

Response:

{
  "status": "healthy",
  "model_loaded": true,
  "model_version": "1.1.0"
}
3️. Prediction Endpoint
POST /predict

Example Request:

{
  "Gender": "Male",
  "Senior_Citizen": 0,
  "Partner": "Yes",
  "Dependents": "No",
  "Phone_Service": "Yes",
  "Multiple_Lines": "No",
  "Internet_Service": "Fiber optic",
  "Online_Security": "No",
  "Online_Backup": "Yes",
  "Device_Protection": "No",
  "Tech_Support": "No",
  "Streaming_TV": "Yes",
  "Streaming_Movies": "Yes",
  "Contract": "Month-to-month",
  "Paperless_Billing": "Yes",
  "Payment_Method": "Electronic check",
  "Tenure_Months": 12,
  "Monthly_Charges": 89.5,
  "Total_Charges": 1200
}

Example Response:

{
  "prediction": 1,
  "churn_probability": 0.65,
  "model_version": "1.1.0"
}
Production Engineering Features

This project includes:

Structured JSON logging

Unique request ID middleware

Latency tracking middleware

Model version exposure in responses

Docker multi-platform builds (linux/amd64)

Automated CI/CD pipeline

Cloud deployment on Render

Version-controlled Docker image tags

This demonstrates production-level ML system design.

🐳 Docker

Docker Hub Repository:

https://hub.docker.com/r/lalitha1020/churn-api

Pull image:

docker pull lalitha1020/churn-api:1.1.0

Build manually:

docker buildx build \
  --platform linux/amd64 \
  -t lalitha1020/churn-api:1.1.0 \
  --push .
 CI/CD Pipeline

**Repository:**

https://github.com/alapatilalitha/Customer-churn-prediction

**Workflow file:**

.github/workflows/docker.yml

On every push to main:

GitHub Actions triggers

Docker image builds automatically

Image pushes to Docker Hub

Render pulls updated image

Service redeploys

This ensures reproducible, automated deployments.

**Local Development**

**Clone repository:**

git clone https://github.com/alapatilalitha/Customer-churn-prediction.git

cd Customer-churn-prediction

**Create virtual environment:**

python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

**Run locally:**

uvicorn app:app --reload

**Access Swagger:**

http://127.0.0.1:8000/docs

 Repository Structure
Customer-churn-prediction/
│
├── app.py
├── train.py
├── model.pkl
├── Dockerfile
├── requirements.txt
├── README.md
├── .gitignore
├── screenshots/
│     ├── swagger.png
│     ├── health.png
│     └── predict.png
└── .github/
      └── workflows/
            └── docker.yml

**Screenshots**

Swagger UI

Health Endpoint

Sample Prediction