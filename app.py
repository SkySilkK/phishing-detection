from flask import Flask, render_template, request
from feature_extraction import extract_features
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/predict", methods=["POST"])
def predict():
    url = request.form.get("url")
    features = extract_features(url)

    print("URL Received:", url)
    print("Features:", features)
    return "POST is working"

if __name__ == "__main__":
    app.run(debug=True)

