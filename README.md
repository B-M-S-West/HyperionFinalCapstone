# Sentiment Analysis Script

This script performs sentiment analysis on Amazon product reviews using the spaCy library and the TextBlob sentiment analysis model.

## Installation

To run this script, you need to have Python installed. Additionally, you need to install the following dependencies:

- pandas
- spacy
- spacytextblob

You can install these dependencies using pip:

`pip install pandas spacy spacytextblob`


## Usage

To use this script, follow these steps:

1. Download the `amazon_product_review.csv` file and place it in the same directory as the script.
2. Open a terminal or command prompt and navigate to the directory containing the script.
3. Run the script using the following command:

`python sentiment_analysis.py`

4. The script will preprocess the reviews, predict the sentiment of a selected review, and compare the similarity between two reviews.
5. The sentiment of the selected review and the similarity score between the two reviews will be displayed in the console.

## Example

Here is an example of how to use the script:

$ python sentiment_analysis.py
Review to test: This product is amazing!
The sentiment of the review is: Positive
The similarity score between the two selected reviews is: 0.85


## Notes

- The script uses the spaCy library and the TextBlob sentiment analysis model to perform sentiment analysis.
- The `amazon_product_review.csv` file should contain a column named 'reviews.text' with the product reviews.
- Missing values in the 'reviews.text' column will be removed before preprocessing.
- The script uses the spaCy 'en_core_web_sm' model for text preprocessing.
- The script requires an internet connection to download the spaCy model and the TextBlob sentiment analysis model.