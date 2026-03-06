import mlflow

model = mlflow.pyfunc.load_model(
    "models:/ChurnPredictionModel@production"
)

print("Model loaded successfully")