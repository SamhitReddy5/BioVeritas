import pickle

model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

def predict(sentences):
    X = vectorizer.transform(sentences)
    return model.predict_proba(X)[:,1]