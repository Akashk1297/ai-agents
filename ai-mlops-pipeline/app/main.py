from fastapi import FastAPI
import joblib
import numpy as np
from pydantic import BaseModel

app = FastAPI()

model = joblib.load("models/model.pkl")

class IrisRequest(BaseModel):
    features: list

@app.get("/")
def health():
    return {"status": "ok"}

@app.post("/predict")
def predict(request: IrisRequest):
    data = np.array(request.features).reshape(1, -1)
    prediction = model.predict(data)
    return {"prediction": int(prediction[0])}