import pandas as pd
import joblib
from Backend.preprocess import load_and_preprocess_data
from Backend.features_eng import add_advanced_feautures
from Backend.train_model import train_model

X_resampled, y_resampled, scaler = load_and_preprocess_data('data/dataset.csv')

joblib.dump(scaler, 'model/scaler.pkl')


