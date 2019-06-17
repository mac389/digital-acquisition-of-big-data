<div id="toc"/>
## Table of Contents

 [Day 1: Setting the Stage](#day-1)<br>
 [Day 2: JSON Data](#day-2)<br>
 [Day 3: XML Data](#day-3)<br>
 [Day 4: The Rest of the Pipeline](#day-4)<br>
 [Day 5: Next Steps](#day-5)<br> 

--
<div id="day-1"/>
## Setting the Stage (Day 1)
[Back to Table of Contents](#toc)

### [Python](https://www.python.org/) & [Sublime Text](https://www.sublimetext.com/)

 Python is a programming language. Idiomatic Python reads close to English ([style guide]("https://docs.python-guide.org/writing/style/")).



### What is an Application Programming Interface (API)?

 An application programming interface refers to the protocols programs use to exchange data. 
 
 ```
from twython import Twython  
import json

# Load credentials from json file
with open("twitter_credentials.json", "r") as file:  
    creds = json.load(file)

# Instantiate an object
python_tweets = Twython(creds['CONSUMER_KEY'], creds['CONSUMER_SECRET'])

# Create our query
query = {'q': 'learn python',  
        'result_type': 'popular',
        'count': 10,
        'lang': 'en',
        }
 ```

### What's underneath the hood of a Twitter page?

  Twitter's API provides tweets as JSON objects ([specification](https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/intro-to-tweet-json.html))

```
{
	"created_at": "Thu May 10 17:41:57 +0000 2018",
	"id_str": "994633657141813248",
	"text": "Just another Extended Tweet with more than 140 characters, generated as a documentation example, showing that [\"tru… https://t.co/U7Se4NM7Eu",
	"display_text_range": [0, 140],
	"truncated": true,
	"user": {
		"id_str": "944480690",
		"screen_name": "FloodSocial"
	},
	"extended_tweet": {
		"full_text": "Just another Extended Tweet with more than 140 characters, generated as a documentation example, showing that [\"truncated\": true] and the presence of an \"extended_tweet\" object with complete text and \"entities\" #documentation #parsingJSON #GeoTagged https://t.co/e9yhQTJSIA",
		"display_text_range": [0, 249],
		"entities": {
			"hashtags": [{
				"text": "documentation",
				"indices": [211, 225]
			}, {
				"text": "parsingJSON",
				"indices": [226, 238]
			}, {
				"text": "GeoTagged",
				"indices": [239, 249]
			}]
		}

	},
	"entities": {
		"hashtags": []
	}
}


```


### Delivering Data verus Syndromic Surveillance

 Twitter provides varying levels of access depending on how much one can pay. Completely free access provides a 1% random sample of streaming tweets. The sampling methodology is not clear. It is for example not known how long one must weight in between sampling for the two samples to be independent. 
 
  Twitter's approach is not unique. Social media web sites (and their APIs) are meant to let other applications access current data. Sampling is provided to allow devices with low bandwidth to recieve data, not to support statistical inference. 
  
  **Geographic bias** The geographic information over-represents urban areas[^1]. 


[^1]: @inproceedings{hecht2014tale,
  title={A tale of cities: Urban biases in volunteered geographic information},
  author={Hecht, Brent and Stephens, Monica},
  booktitle={Eighth International AAAI Conference on Weblogs and Social Media},
  year={2014}}

## Acquiring JSON Data (Day 2)
[Back to Table of Contents](#toc)

1. Streaming versus Historical Data [Twitter package](https://stackabuse.com/accessing-the-twitter-api-with-python/)
2. The `json` package
3. Good code is the same thing as readable code
4. Storage
5. Project Management, including How do I hand off a prototype


<div id="day-3"/>
## Acquiring XML Data (Day 3)
[Back to Table of Contents](#toc)

2. Who still uses XML?
3. Structure of XML data.
4. `BeautifulSoup` and `lxml`

<div id="day-4"/>
## How does this fit with what I usually do? (Day 4)
[Back to Table of Contents](#toc)

### Converting Internet data to CSV using  `csv` or DataFrames using  `pandas` 

```
import pandas as pd

# Search tweets
dict_ = {'user': [], 'date': [], 'text': [], 'favorite_count': []}  
for status in python_tweets.search(**query)['statuses']:  
    dict_['user'].append(status['user']['screen_name'])
    dict_['date'].append(status['created_at'])
    dict_['text'].append(status['text'])
    dict_['favorite_count'].append(status['favorite_count'])

# Structure data in a pandas DataFrame for easier manipulation
df = pd.DataFrame(dict_)  
df.sort_values(by='favorite_count', inplace=True, ascending=False)  
df.head(5)
```

2. Graphing with `seaborn`, `matplotlib`
3. What are binary files? 
4. What is `MongoDB`, `MySQL`?

<div id="day-5"/>
## Where do I go from here? (Day 5)
[Back to Table of Contents](#toc)

1. Study Design
2. What Journals?
3. What Conferences?
4. What Grants?
5. What Collaborators?



### Housekeeping 

 1. [How to open an issue on GitHub](https://help.github.com/en/articles/creating-an-issue)
 1. [How to fork a repo](https://help.github.com/en/articles/fork-a-repo)
 1. [Download the Desktop app for GitHub](https://desktop.github.com/)
 1. [Install Python](https://www.python.org/downloads/)
 1. [Install Sublime Text **(Mac)**](https://www.sublimetext.com/)  -or- [Install Notepad++ **(PC)**](https://notepad-plus-plus.org/)
