import gradio as gr
import numpy as np
from sklearn.linear_model import LogisticRegression

# ---------------- MODEL ----------------
X = np.array([
    [1,1,1,1],
    [1,0,1,1],
    [1,1,0,1],
    [0,0,0,0],
    [0,0,0,1],
    [0,0,1,0],
    [1,1,1,0],
    [0,1,0,0]
])

y = np.array([1,1,1,0,0,0,1,0])

model = LogisticRegression()
model.fit(X, y)

# ---------------- FEATURE EXTRACTION ----------------
def extract_features(url):
    url_length = 1 if len(url) > 30 else 0
    has_at = 1 if "@" in url else 0
    has_dash = 1 if "-" in url else 0
    too_many_dots = 1 if url.count(".") > 2 else 0
    return np.array([[url_length, has_at, has_dash, too_many_dots]])

# ---------------- PREDICTION ----------------
def predict(url):
    features = extract_features(url)
    prediction = model.predict(features)

    return "⚠️ PHISHING WEBSITE" if prediction[0] == 1 else "✅ SAFE WEBSITE"

# ---------------- UI ----------------
gr.Interface(
    fn=predict,
    inputs=gr.Textbox(label="Enter Website URL"),
    outputs="text",
    title="🔐 Phishing Website Detector",
    description="Check whether a URL is Safe or Phishing"
).launch()