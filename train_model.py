import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

# Sample data (for testing)
data = {
    "url": [
        "http://www.google.com",
        "http://login.microsoft.xyz/fakepage",
        "https://secure.paypal.com",
        "http://verify-paypal.com",
        "https://accounts.google.com",
        "http://bankofamerica.secure-login.com"
    ],
    "label": [0, 1, 0, 1, 0, 1]  # 0 = Legitimate, 1 = Phishing
}

df = pd.DataFrame(data)

# Feature extraction
df["url_length"] = df["url"].apply(len)
df["dot_count"] = df["url"].apply(lambda x: x.count('.'))
df["hyphen_count"] = df["url"].apply(lambda x: x.count('-'))

X = df[["url_length", "dot_count", "hyphen_count"]]
y = df["label"]

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save model
joblib.dump(model, "model.pkl")
print("✅ Model trained and saved as model.pkl")
