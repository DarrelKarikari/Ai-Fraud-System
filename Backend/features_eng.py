import pandas as pd
from sklearn.preprocessing import PolynomialFeatures

def add_advanced_feautures(df):
    poly = PolynomialFeatures(degree=2, interaction_only=True, include_bias=False)
    X_poly = poly.fit_transform(df)
    df['transaction_hour'] = pd.to_datetime(df['Time'], unit='s').dt.hour
    df['is_weekend'] = pd.to_datetime(df['Time'], unit='s').dt.weekday >= 5
    return df, X_poly