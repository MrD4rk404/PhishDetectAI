# PhishDetectAI - Phishing URL Classifier

## Overview
PhishDetectAI is a machine learning-based web app built with Streamlit that detects whether a URL is phishing or legitimate.

## Features
- Enter a URL and receive instant prediction
- Uses machine learning model trained on phishing dataset
- Simple web interface using Streamlit

## Tech Stack
- Python
- Streamlit
- Scikit-learn
- Pandas
- Joblib

## How to Run
1. Clone or extract the project folder
2. Open command prompt in the folder and run:
   ```bash
   pip install -r requirements.txt
   python train_model.py
   streamlit run app.py
