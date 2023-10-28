from fastapi import FastAPI, HTTPException, status
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
from app.schemas import CropInput
import pandas as pd
import numpy as np
import pickle


app = FastAPI(
    title="Crop Recommendation",
    description="Crop Recommendation is an application that provides personalized crop recommendations based on soil and environmental conditions. It helps farmers and agricultural enthusiasts make informed decisions on which crops to grow in a specific season. By inputting data on soil properties (N, P, K), temperature, humidity, pH, and rainfall, the application uses a machine learning model to predict the most suitable crops for cultivation. This project aims to optimize agricultural yield and promote sustainable farming practices.",
)

with open("crop_recommendation.pkl", 'rb') as f:
    model = pickle.load(f)

with open("standard_scaler.pkl", 'rb') as scaler_file:
    sc = pickle.load(scaler_file)

with open("label_encoder.pkl", 'rb') as label_encoder_file:
    le = pickle.load(label_encoder_file)


@app.get('/')
def home():
    return "Welcome to Crop Recommendation application"

@app.post('/recommend')
async def recommend(request: CropInput):
    # Create a dictionary with user input values
    input_data = {
        'N': [request.N],
        'P': [request.P],
        'K': [request.K],
        'temperature': [request.temperature],
        'humidity': [request.humidity],
        'ph': [request.pH],
        'rainfall': [request.rainfall]
    }

    # Create a DataFrame from the input data
    input_df = pd.DataFrame(input_data)

    # Standardize the input data using the same StandardScaler used for training data
    input_df = sc.transform(input_df)

    # Use the trained model to make crop recommendations
    recommended_label = model.predict(input_df)

    # Decode the predicted label using the LabelEncoder
    recommended_crop = le.inverse_transform(recommended_label)

    return {
        "Recommended Crops": recommended_crop.tolist()
    }
