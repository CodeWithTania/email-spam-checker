import pandas as pd
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSV_PATH = os.path.join(BASE_DIR, "spam.csv")

data = pd.read_csv(CSV_PATH)

# DEBUG check (important)
print("CSV Columns:", data.columns)

data.columns = data.columns.str.strip().str.lower()
data = data[['label', 'text']]
data['label'] = data['label'].astype(int)

vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(data['text'])
y = data['label']

model = MultinomialNB()
model.fit(X, y)

def predict_email(message):
    msg_vec = vectorizer.transform([message])
    prediction = model.predict(msg_vec)[0]
    return "Spam" if prediction == 1 else "Ham"
