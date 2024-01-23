# Capstone Project - Sentiment Analysis
import pandas as pd
import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from spacytextblob.spacytextblob import SpacyTextBlob

# Load the spaCy model
nlp = spacy.load('en_core_web_sm')
nlp.add_pipe('spacytextblob')

# Load the data from the CSV file
data = pd.read_csv('amazon_product_review.csv')

# Select 'reviews.text' column and remove missing values
clean_data = data['reviews.text'].dropna()

# function to preprocess text
def preprocess_text(text):
    doc = nlp(text)
    return ' '.join([token.lemma_ for token in doc if not token.is_stop])


# Apply the preprocessing function to the 'review.text' column
clean_data = clean_data.apply(preprocess_text)

# Function to predict sentiment
def predict_sentiment(text):
    doc = nlp(text)
    if doc._.polarity > 0:
        return 'Positive'
    elif doc._.polarity < 0:
        return 'Negative'
    else:
        return 'Neutral'


# function to compare similarity between two reviews
def compare_similarity(review1, review2):
    doc1 = nlp(review1)
    doc2 = nlp(review2)
    return doc1.similarity(doc2)

#select a single review to test the function
review_to_test = clean_data.iloc[0]
print("Review to test:", review_to_test)

# Apply sentiment prediction to preprocessed reviews
sentiments = predict_sentiment(review_to_test)
print(f"The sentiment of the review is: {sentiments}")

# Select two reviews to compare
review1 = clean_data.iloc[0]
review2 = clean_data.iloc[1]

# Compare similarity between the two selected reviews
similarity_score = compare_similarity(review1, review2)

print(f"The similarity score between the two selected reviews is: {similarity_score}")
