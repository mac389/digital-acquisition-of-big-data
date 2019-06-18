from twython import Twython  
import json

# Load credentials from json file
with open("twitter_credentials.json", "r") as file:  
    creds = json.load(file)

# Instantiate an object
python_tweets = Twython(creds['CONSUMER_KEY'], creds['CONSUMER_SECRET'])

# Create our query

query = {'q': '911',  
        'count': 3
        }

search_results = python_tweets.search(**query)

json.dump(search_results,open('data2.json','w'))

data = json.load(open('./data.json','r'))

import pandas as pd

tweet_texts = [item["text"].encode('utf8') for item in data["statuses"]]

df = pd.DataFrame(tweet_texts, columns=['text'])

df.to_csv('./tweets-qua-csv',index=False)
print 'Done'
