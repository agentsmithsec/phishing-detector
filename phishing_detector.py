import joblib

def extract_features(url):
    return [
        len(url),
        int('@' in url),
        int(url.count('//') > 1),
        url.count('.')
    ]

def predict_url(url):
    model = joblib.load('phishing_model.joblib')
    features = [extract_features(url)]
    prediction = model.predict(features)
    return "Phishing" if prediction[0] == 1 else "Safe"

if __name__ == "__main__":
    test_url = input("Enter URL to check: ")
    result = predict_url(test_url)
    print(f"The URL is: {result}")
