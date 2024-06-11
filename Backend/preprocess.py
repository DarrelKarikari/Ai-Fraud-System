import pandas as pd
from sklearn.preprocessing import StandardScaler
from imblearn.over_sampling import SMOTE

file_path = 'data/dataset.csv'

def load_and_preprocess_data(file_path):
    df = pd.read_csv(file_path)
    df.fillna(method='ffill', inplace=True)
    scaler= StandardScaler()
    df[['Amount','Time']]= scaler.fit_transform(df[['Amount','Time']])
    X=df.drop(columns=['Class'])
    y= df['Class']
    smote= SMOTE(random_state=42)
    X_resampled, y_resampled= smote.fit_resample(X,y)
    return X_resampled, y_resampled, scaler