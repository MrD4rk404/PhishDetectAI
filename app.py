import streamlit as st
import joblib

# Load trained model
model = joblib.load("model.pkl")

st.title("PhishDetectAI - Phishing URL Classifier")

# User input
url = st.text_input("Enter the URL to check:")

if st.button("Predict"):
    if url:
        # Dummy feature extraction (replace with actual method if needed)
        features = [len(url), url.count('.'), url.count('-')]
        prediction = model.predict([features])
        result = "Phishing" if prediction[0] == 1 else "Legitimate"
        st.success(f"The URL is likely: **{result}**")
    else:
        st.warning("Please enter a URL.")
