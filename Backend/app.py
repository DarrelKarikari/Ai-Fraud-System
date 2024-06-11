import argparse
from flask import Flask, request, jsonify
import joblib
import pandas as pd
from Backend.preprocess import load_and_preprocess_data
from Backend.features_eng import add_advanced_features

app = Flask(__name__)
model = joblib.load('model/advanced_fraud_detection_model.pkl')
scaler = joblib.load('model/scaler.pkl')  

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    data_df = pd.DataFrame(data, index=[0])
    data_df[['Amount', 'Time']] = scaler.transform(data_df[['Amount', 'Time']])
    data_df, _ = add_advanced_features(data_df)
    prediction = model.predict(data_df)
    return jsonify({'prediction': prediction.tolist()})

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Flask App for Fraud Detection")
    parser.add_argument('--port', type=int, default=5000, help="Port number")
    args = parser.parse_args()
    app.run(debug=True, port=args.port)
