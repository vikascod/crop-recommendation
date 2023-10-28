# Crop Recommendation System

This project is a Crop Recommendation System that helps farmers make informed decisions about which crops to cultivate based on soil and environmental conditions.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Data Source](#data-source)
- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Model Training](#model-training)
- [Model Evaluation](#model-evaluation)
- [Predictive System](#predictive-system)
- [Saving the Model](#saving-the-model)

## Introduction
Agriculture is a vital sector for any country. The Crop Recommendation System aims to assist farmers in selecting the most suitable crops to plant based on soil quality and environmental factors. The system is built using machine learning techniques and allows farmers to input their soil and climate conditions to receive crop recommendations.

## Features
- Predicts suitable crops based on soil and climate data.
- Provides information about the best crop for a given set of conditions.

## Data Source
The dataset used for training and testing the model is available on Kaggle:
[Crop Recommendation Dataset](https://www.kaggle.com/datasets/atharvaingle/crop-recommendation-dataset)

## Prerequisites
Before running the system, you'll need to install the required Python libraries. You can do this using pip:

1. Clone the repository:

    ```bash
    git clone https://github.com/vikascod/crop-recommendation
    cd crop-recommendation

2. Install the project dependencies:

   ```bash
   pip install -r requirements.txt

- Download the dataset from the provided Kaggle link and save it as Crop_recommendation.csv in the project directory.

## Usage
- Open and run the Jupyter Notebook Crop_Recommendation.ipynb to train the model and explore the data.

## Model Training
- The Jupyter Notebook contains the code for data preprocessing, model training, and evaluation.

## Model Evaluation
- The model is evaluated using accuracy and cross-validation scores. The best model is selected using GridSearchCV.

## Predictive System
- The predictive system allows users to input their soil and climate data and receive crop recommendations.

## Saving the Model
- The trained model, StandardScaler, and LabelEncoder are saved to the crop_recommendation_model.pkl file. You can load this model for future predictions.

