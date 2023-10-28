from fastapi import FastAPI, HTTPException, status
from app.schemas import CropInput
import numpy as np
import pickle

app = FastAPI(
    title="Crop Recommendation",
    description="Crop Recommendation is an application that provides personalized crop recommendations based on soil and environmental conditions. It helps farmers and agricultural enthusiasts make informed decisions on which crops to grow in a specific season. By inputting data on soil properties (N, P, K), temperature, humidity, pH, and rainfall, the application uses a machine learning model to predict the most suitable crops for cultivation. This project aims to optimize agricultural yield and promote sustainable farming practices.",
)

# Load the machine learning model from the pickle file
with open("crop_recommendation.pkl", 'rb') as f:
    model = pickle.load(f)

@app.get('/')
def home():
    return "Welcome to Crop Recommendation application"

@app.post('/recommend')
async def recommend(request: CropInput):
    try:
        N = float(request.N)
        P = float(request.P)
        K = float(request.K)
        temperature = float(request.temperature)
        humidity = float(request.humidity)
        pH = float(request.pH)
        rainfall = float(request.rainfall)

        input_data = [[N, P, K, temperature, humidity, pH, rainfall]]

        predicted_crop = model.predict(input_data)
        return {"recommended_crop": predicted_crop[0]}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Unable to predict")
