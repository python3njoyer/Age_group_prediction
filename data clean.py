import csv
import re
from cleantext import clean


path = 'Zendaya.csv'

# import tweet dataset from csv, store tweets line by line in list
user_twts = []

with open(path, encoding='utf-8') as read_file:
    tweet_data = csv.reader(read_file)
    next(tweet_data)
    for row in tweet_data:
        user_twts.append(row[1])


# merge all tweets for one user into a single string
tweet_str = ' '.join(user_twts)
print('Original tweets:', tweet_str)


# remove emoji
tweet_str = clean(tweet_str, no_emoji=True)


# change uppercase letters to lowercase, ignoring emoticons
emoticons = [':D', 'XD', ':P', ';D', 'XP', ':D D', '=D', '=P']

save_emot = []
for i in emoticons:
    if i in tweet_str:
        save_emot.append(i)
        tweet_str = re.sub(i, '', tweet_str)  # remove emoticons with capital letters from tweets

tweet_str = tweet_str.lower()  # turn all remaining char in tweets lowercase
tweet_str = tweet_str + ' ' + ' '.join(save_emot)  # add emoticons with capital letters back in
print('Cleaned tweets:', tweet_str)


# write tweets to csv file
filename = path[:-4] + '_cleaned.csv'
with open(filename, 'w') as new_txt:
    new_txt.write(tweet_str)
