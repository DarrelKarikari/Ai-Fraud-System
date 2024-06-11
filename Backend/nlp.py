import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

def add_nlp_features(text_data):
    vectorizer = TfidfVectorizer()
    X_text = vectorizer.fit_transform(text_data['text_column'])
    text_features_df = pd.DataFrame(X_text.toarray(), columns=vectorizer.get_feature_names_out())
    return text_features_df

nlp_features =add_nlp_features()