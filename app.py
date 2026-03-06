from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import pandas as pd
import logging

# ----------------------------
# Logging Configuration
# ----------------------------
logging.basicConfig(
    filename="prediction_logs.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

app = FastAPI()

# ----------------------------
# Load Model
# ----------------------------
model = joblib.load("model.pkl")
MODEL_VERSION = "1.1.0"

# ----------------------------
# Request Schema
# ----------------------------
class ChurnRequest(BaseModel):
    Gender: str
    Senior_Citizen: str
    Partner: str
    Dependents: str
    Phone_Service: str
    Multiple_Lines: str
    Internet_Service: str
    Online_Security: str
    Online_Backup: str
    Device_Protection: str
    Tech_Support: str
    Streaming_TV: str
    Streaming_Movies: str
    Contract: str
    Paperless_Billing: str
    Payment_Method: str
    Tenure_Months: int
    Monthly_Charges: float
    Total_Charges: float


# ----------------------------
# Response Schema
# ----------------------------
class PredictionResponse(BaseModel):
    prediction: int
    churn_probability: float
    model_version: str


# ----------------------------
# Basic Endpoints
# ----------------------------
# ----------------------------
# Basic Endpoints
# ----------------------------

@app.get("/")
def home():
    return {
        "message": "Customer Churn Prediction API",
        "version": MODEL_VERSION
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "model_loaded": model is not None,
        "model_version": MODEL_VERSION
    }


@app.get("/model-info")
def model_info():
    return {
        "model_type": type(model.named_steps["classifier"]).__name__,
        "model_version": MODEL_VERSION,
        "total_input_features": len(
            model.named_steps["preprocessor"].feature_names_in_
        )
    }

# ----------------------------
# Prediction Endpoint
# ----------------------------
@app.post("/predict", response_model=PredictionResponse)
def predict(data: ChurnRequest):
    try:
        # Convert request to DataFrame
        df = pd.DataFrame([data.dict()])

        # Rename columns to EXACT training column names
        df = df.rename(columns={
            "Senior_Citizen": "Senior Citizen",
            "Phone_Service": "Phone Service",
            "Multiple_Lines": "Multiple Lines",
            "Internet_Service": "Internet Service",
            "Online_Security": "Online Security",
            "Online_Backup": "Online Backup",
            "Device_Protection": "Device Protection",
            "Tech_Support": "Tech Support",
            "Streaming_TV": "Streaming TV",
            "Streaming_Movies": "Streaming Movies",
            "Paperless_Billing": "Paperless Billing",
            "Payment_Method": "Payment Method",
            "Tenure_Months": "Tenure Months",
            "Monthly_Charges": "Monthly Charges",
            "Total_Charges": "Total Charges"
        })

        # Ensure column order matches training data
        df = df[[
            "Gender",
            "Senior Citizen",
            "Partner",
            "Dependents",
            "Phone Service",
            "Multiple Lines",
            "Internet Service",
            "Online Security",
            "Online Backup",
            "Device Protection",
            "Tech Support",
            "Streaming TV",
            "Streaming Movies",
            "Contract",
            "Paperless Billing",
            "Payment Method",
            "Tenure Months",
            "Monthly Charges",
            "Total Charges"
        ]]

        # Make prediction
        prediction = model.predict(df)[0]
        probability = model.predict_proba(df)[0][1]

        # Log prediction
        logging.info(
            f"Input: {data.dict()} | Prediction: {prediction} | Probability: {probability}"
        )

        return {
            "prediction": int(prediction),
            "churn_probability": float(probability),
            "model_version": MODEL_VERSION
        }

    except Exception as e:
        logging.error(f"Prediction error: {str(e)}")
        raise HTTPException(status_code=500, detail="Prediction failed")