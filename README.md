# Twitter Age Prediction

This project is based off lexica constructed by the World Well Being Project. The purpose of the present project is to apply the lexica to build a predictive model of age from language use. The model was tested on celebrity tweets, as their Twitter activity and age are easily accessible, but the same algorithm can be applied to other social media datasets.

Steps:
1. Download lexica for four age bins: https://github.com/wwbp/word_and_phrase_correlations/tree/master/csv
2. Download celebrity tweet dataset: https://github.com/estorrs/twitter-celebrity-tweet-sentiment/blob/master/results/celebrity_tweets_results.csv
3. Split celebrity tweet dataset into separate csv file for each celebrity
4. Clean celebrity tweets with data_clean.py
5. Run logistic regression with regression.py 
