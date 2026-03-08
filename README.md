#  Customer Churn Prediction API

## Production-Ready ML Service with Docker, CI/CD & Cloud Deployment

##  Business Problem

Customer churn significantly impacts revenue in telecom businesses.

The objective of this system is to predict whether a customer is likely to churn so that businesses can:

- Identify high-risk customers

- Design targeted retention campaigns

- Reduce revenue loss

- Improve customer lifetime value

## Model Details

- **Algorithm:** Scikit-learn Classification Model

- **Target:** Binary classification (Churn / No Churn)

- **Serialization:** joblib

- **API Framework:** FastAPI

- **Model Versioning:** Enabled

The model is trained on the IBM Telco Customer Churn dataset.

## Model Evaluation

Dataset

**Source:** IBM Telco Customer Churn Dataset

**Type:** Binary classification

**Target variable:** Churn

| Metric    | Score |
| --------- | ----- |
| Accuracy  | ~0.82 |
| Precision | ~0.79 |
| Recall    | ~0.75 |
| F1 Score  | ~0.77 |
| ROC-AUC   | ~0.84 |

Metrics may vary slightly depending on random state and preprocessing.

## Why These Metrics Matter

- Accuracy measures overall correctness.

- Recall is critical because missing churn customers directly impacts revenue.

- F1 Score balances precision and recall.

- ROC-AUC measures class separation capability.

This demonstrates thoughtful evaluation beyond simple accuracy reporting.

## System Architecture

Client Request → FastAPI Service → Model Inference → Structured JSON Response

## CI/CD Flow

GitHub → GitHub Actions → Docker Image Build (linux/amd64) → Docker Hub → Render Deployment

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

## Live Deployment
**Production API**

https://churn-api-fayv.onrender.com

**Swagger Documentation**

https://churn-api-fayv.onrender.com/docs

**Health Endpoint**

https://churn-api-fayv.onrender.com/health

**API Endpoints**
- Root Endpoint

GET /

Response:
{
  "message": "Customer Churn Prediction API",
  "version": "1.1.0"
}

-  Health Check

GET /health

Used for production monitoring.

Response:
{
  "status": "healthy",
  "model_loaded": true,
  "model_version": "1.1.0"
}

- Prediction Endpoint

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
{
  "prediction": 1,
  "churn_probability": 0.65,
  "model_version": "1.1.0"
}

## Production Engineering Features

This project includes:

- Structured JSON logging

- Unique request ID middleware

- Latency tracking middleware

- Model version exposure in responses

- Docker multi-platform builds (linux/amd64)

- Automated CI/CD pipeline

- Cloud deployment on Render

- Version-controlled Docker image tags

This demonstrates production-level ML system design.

## Docker

**Docker Hub Repository:**

https://hub.docker.com/r/lalitha1020/churn-api

**Pull image:**
docker pull lalitha1020/churn-api:1.1.0

**Build manually:**
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

- GitHub Actions triggers

- Docker image builds automatically

- Image pushes to Docker Hub

- Render pulls updated image

- Service redeploys

This ensures reproducible, automated deployments.

## Local Development

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

**Repository Structure**
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
│   ├── swagger-ui.png
│   ├── local-predicion.png
│   └── render-health.png
└── .github/
    └── workflows/
        └── docker.yml

## Screenshots

### Swagger UI
![Swagger UI](screenshots/swagger-ui.png)

### Local Prediction
![Local Prediction](screenshots/local-prediction.png)

### Render Health Endpoint
![Render Health](screenshots/render-health.png)

### Render Root Endpoint
![Render Root](screenshots/render-root.png)
