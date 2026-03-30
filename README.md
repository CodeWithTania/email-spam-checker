# 📧 Intelligent Email Spam Checker (NLP)

"An Intelligent Email Spam Detection system using Python, Scikit-Learn, and NLP. Classifies messages as Spam or Ham with high accuracy using the Naive Bayes algorithm."

---

## 📖 Project Overview
Spam detection is a classic problem in Machine Learning. This tool uses a **Multinomial Naive Bayes** classifier to analyze text patterns. It processes raw email data, cleans it using NLP techniques, and predicts whether a message is safe or a threat.

## 🚀 Key Features
- **Text Preprocessing:** Automated cleaning, stop-word removal, and tokenization.
- **Efficient Vectorization:** Uses `CountVectorizer` to convert text into numerical features.
- **Real-time Prediction:** Fast and accurate classification for any input text.
- **Data Driven:** Trained on labeled datasets for high precision.

---

## 📂 Project Structure
```text
email-spam-checker/
│
├── main.py              # The primary script for training/prediction
├── spam.csv             # Dataset containing Spam and Ham labels
├── README.md            # Detailed project documentation
└── requirements.txt     # Essential Python libraries
