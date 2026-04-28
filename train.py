import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

def train_model():
    df = pd.read_csv("dataset/data.csv")

    vectorizer = TfidfVectorizer(ngram_range=(1,3))
    X = vectorizer.fit_transform(df["text"])
    y = df["label"]

    # IMPORTANT FIX
    model = LogisticRegression(class_weight='balanced', max_iter=1000)
    model.fit(X, y)

    pickle.dump(model, open("model.pkl", "wb"))
    pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))

    print("✅ Model trained successfully")

if __name__ == "__main__":
    train_model()