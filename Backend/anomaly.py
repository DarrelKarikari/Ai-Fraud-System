import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.feature_extraction.text import TfidfVectorizer

def add_anomaly_feature(text_data):
    vectorizer = TfidfVectorizer()
    X_text = vectorizer.fit_transform(text_data['text_column'])
    isolation_forest = IsolationForest()
    isolation_forest.fit(X_text)
    anomaly_predictions = isolation_forest.predict(X_text)
    text_data['anomaly'] = anomaly_predictions
    return text_data

text_data= add_anomaly_feature()