# Apex Legends Sentiment Analysis

This project analyzes Steam user reviews of Apex Legends and builds a sentiment classification model to predict whether a review is positive or negative.

## Notebook

- `Apex_Legends_Sentiment_Analysis.ipynb`: End-to-end workflow from data loading to model evaluation.

## Data Collection (Scraping)

- `scrape_apex_reviews.py`: Script used to scrape Apex Legends Steam reviews using `steamreviews`.
- Raw scraped file: `data/review_1172470.json`
- Analysis dataset: `review_1172470.csv`

## Dataset

- `review_1172470.csv`: Raw Steam review dataset used in this project.

## Project Workflow

1. Load and inspect the dataset.
2. Apply text preprocessing in this order:
   - Cleansing (remove URL, punctuation, and extra spaces)
   - Case folding
   - Tokenizing
   - Filtering (remove stopwords and single-character tokens)
   - Stemming using Porter Stemmer
3. Perform exploratory data analysis (EDA).
4. Split data into training and test sets with stratification.
5. Handle class imbalance on training data with minority upsampling.
6. Train a Word2Vec + Multinomial Naive Bayes model.
7. Evaluate with accuracy, classification report, and confusion matrix.

## Installation

```bash
pip install -r requirements.txt
```

## Run

Open and run `Apex_Legends_Sentiment_Analysis.ipynb` in Jupyter Notebook or VS Code.

To re-scrape the dataset:

```bash
python scrape_apex_reviews.py
```

## Model Notes

- Class imbalance handling is applied only to the training split (minority upsampling), not to test data.
- Keeping the test split in its original distribution provides a fairer estimate of real-world performance.
- In addition to accuracy, prioritize macro-average F1 and per-class recall to evaluate minority-class performance.

## Tools and Libraries

- Python
- pandas
- numpy
- scikit-learn
- gensim
- nltk
- steamreviews
- matplotlib
- seaborn
