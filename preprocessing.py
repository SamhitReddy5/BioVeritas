import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import WordNetLemmatizer

# download once
try:
    nltk.data.find('tokenizers/punkt')
except:
    nltk.download('punkt')

try:
    nltk.data.find('tokenizers/punkt_tab')
except:
    nltk.download('punkt_tab')

try:
    nltk.data.find('corpora/stopwords')
except:
    nltk.download('stopwords')

try:
    nltk.data.find('corpora/wordnet')
except:
    nltk.download('wordnet')

lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))

def preprocess_text(text):
    sentences = sent_tokenize(text)
    processed = []

    for sent in sentences:
        words = word_tokenize(sent.lower())
        words = [lemmatizer.lemmatize(w) for w in words if w.isalnum() and w not in stop_words]
        processed.append(" ".join(words))

    return sentences, processed