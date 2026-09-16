from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/predict", methods=["POST"])
def predict():
    url = request.form.get("url")

    print("URL Received:", url)
    return "POST is working"

if __name__ == "__main__":
    app.run(debug=True)

