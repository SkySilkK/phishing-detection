import pandas as pd
from feature_extraction import extract_features
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

df = pd.read_csv("data/balanced_urls.csv")
features = df["url"].apply(extract_features)

feature_df = pd.DataFrame(
    features.tolist(),
    columns=[
        "url_length",
        "dots",
        "hyphens",
        "digits",
        "https"
    ]
)

x = feature_df
y = df["label"]
y = y.map({"legitimate": 0, "phishing": 1})

x_train, x_test, y_train, y_test = train_test_split(
    x,
    y, 
    test_size = 0.2,
    random_state = 42,
    stratify=y,
)

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42,
)

model.fit(x_train, y_train)
y_pred = model.predict(x_test)
cm = confusion_matrix(y_test, y_pred)

print(cm)
print(classification_report(y_test, y_pred))
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

