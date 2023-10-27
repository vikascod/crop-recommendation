from fastapi import FastAPI, HTTPException
from app.schemas import CropInput
import numpy as np
import pandas as pd
import pickle

app = FastAPI(
    title="Crop Recommendation",
    description="Crop Recommendation is an application that provides personalized crop recommendations based on soil and environmental conditions. It helps farmers and agricultural enthusiasts make informed decisions on which crops to grow in a specific season. By inputting data on soil properties (N, P, K), temperature, humidity, pH, and rainfall, the application uses a machine learning model to predict the most suitable crops for cultivation. This project aims to optimize agricultural yield and promote sustainable farming practices.",
)

with open("crop_recommendation.pkl", 'rb') as f:
    model = pickle.load(f)

@app.get('/')
def home():
    return "Welcome to Crop Recommendation application"

@app.post('/recommend')
async def recommend(request: CropInput):
    try:
        N = request.N
        P = request.P
        K = request.K
        temperature = request.temperature
        humidity = request.humidity
        pH = request.pH
        rainfall = request.rainfall

        input_data = [[N, P, K, temperature, humidity, pH, rainfall]]

        predict_crop = model.predict(input_data)
        print(predict_crop)
        return predict_crop[0]
    except Exception as e:
        raise HTTPException(status_code=400, detail="Unable to make a recommendation.")
