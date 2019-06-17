<div id="toc"/>
## Table of Contents

 [Day 1: Setting the Stage](#day-1)
 
  - [Social Media and Public Health Research](#some-and-phr)
  - [Python & Sublime Text](#python-and-sublime-text)
  - [What is an Application Programming Interface?](#what-is-an-api)
 
[Day 2: JSON Data](#day-2)<br>
 [Day 3: XML Data](#day-3)<br>
 [Day 4: The Rest of the Pipeline](#day-4)<br>
 [Day 5: Next Steps](#day-5)<br> 

--

[Prior Literature](./prior-literature.md)

<div id="day-1"/>
## Setting the Stage (Day 1)
[Back to Table of Contents](#toc)

<div id="some-and-phr"/>
### Social Media and Public Health Research

   Social media provide a window into trends in the general population in near real-time. They also provide a means for outreach and to assess the effectiveness of interventions. Analyses of social media have provided insights into the dynamics of drug use[^chary1], the response the natural disasters[^twittertsunami], the dynamics of foodborne illnesses[^chicagofbi]<sup>,</sup>[^jamafbi]<sup>,</sup>[^nemesisfbi] and the dynamics of infectious diseases[^twitterflu]. 
   
   The infrastructure created for social media was meant to share data reliably in the moment, not to support research. This has led to irreproducible results[^googlefluerror] and inference of causation with implausible conceptual models[^skepticsome]. Digital epidemiology holds promise for increasing the reach and rapidity of traditional means of syndromic surveaillance[^salatheperspective]<sup>,</sup>[^asianperspective]
   
   More plausible models and robuse findings could arise if public health researchers could be involved earlier the process of acquiring data from social media. This seminar aims to give public health researchers the tools to develop prototype data analysis pipelines from social media. 
   
[^chary1]: Chary, M., Genes, N., Giraud-Carrier, C., Hanson, C., Nelson, L.S. and Manini, A.F., 2017. Epidemiology from tweets: estimating misuse of prescription opioids in the USA from social media. Journal of Medical Toxicology, 13(4), pp.278-286.

[^twittertsunami]: Murakami, A. and Nasukawa, T., 2012, April. Tweeting about the tsunami?: mining twitter for information on the tohoku earthquake and tsunami. In Proceedings of the 21st International Conference on World Wide Web (pp. 709-710). ACM.

[^chicagofbi]: Harris, J.K., Mansour, R., Choucair, B., Olson, J., Nissen, C. and Bhatt, J., 2014. Health department use of social media to identify foodborne illness—Chicago, Illinois, 2013–2014. MMWR. Morbidity and mortality weekly report, 63(32), p.681.

[^jamafbi]: Kuehn, B.M., 2014. Agencies use social media to track foodborne illness. JAMA, 312(2), pp.117-118.

[^nemesisfbi]: Sadilek, A., Kautz, H., DiPrete, L., Labus, B., Portman, E., Teitel, J. and Silenzio, V., 2016, March. Deploying nEmesis: Preventing foodborne illness by data mining social media. In Twenty-Eighth IAAI Conference.

[^twitterflu]: Aramaki, E., Maskawa, S. and Morita, M., 2011, July. Twitter catches the flu: detecting influenza epidemics using Twitter. In Proceedings of the conference on empirical methods in natural language processing (pp. 1568-1576). Association for Computational Linguistics.

[^googlefluerror]: Butler, Declan. "When Google got flu wrong." Nature News 494, no. 7436 (2013): 155.

[^skepticsome]: Rowland, K., 2012. Epidemiologists put social media in the spotlight. Nature.

[^salatheperspective]: Salathe, M., Bengtsson, L., Bodnar, T.J., Brewer, D.D., Brownstein, J.S., Buckee, C., Campbell, E.M., Cattuto, C., Khandelwal, S., Mabry, P.L. and Vespignani, A., 2012. Digital epidemiology. PLoS computational biology, 8(7), p.e1002616.

[^asianperspective]: Fung, I.C.H., Tse, Z.T.H. and Fu, K.W., 2015. The use of social media in public health surveillance. Western Pacific surveillance and response journal: WPSAR, 6(2), p.3.


<div id="python-and-sublime-text"/>
### [Python](https://www.python.org/) & [Sublime Text](https://www.sublimetext.com/)

 Python is a programming language. Idiomatic Python reads close to English ([style guide]("https://docs.python-guide.org/writing/style/")).
 
 ```
 print "Hello World" 
 ```


<div id="what-is-an-api"/>
### What is an Application Programming Interface (API)?

 An application programming interface refers to the protocols programs use to exchange data. An API allows a data source (*e.g* Twitter) to serve data to a user. Those data are available to a user after logging in. Logging in allows the data source to track and regulate the distribution of its data. 

Most APIs require two keys to login. Roughly speaking, one key identifies yourself. The second confirms your identity. ([A deeper explanation](https://stackoverflow.com/questions/11557985/why-use-an-api-key-and-secret)) 
 
There are many Python wrappers to Twitter's API ([overview](https://stackabuse.com/accessing-the-twitter-api-with-python/)).  
 
 
```
from twython import Twython  
import json

# Load credentials from json file
with open("twitter_credentials.json", "r") as file:  
    creds = json.load(file)

# Instantiate an object
api = Twython(creds['CONSUMER_KEY'], creds['CONSUMER_SECRET'])

# Create our query
query = {'q': 'learn python',  
        'result_type': 'popular',
        'count': 10,
        'lang': 'en',
        }
        
api.search(q)
```

The code block above demonstrates how to access Twitter's api via the *twython* wrapper. 


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

| Web site | Link to Python wrapper|
|--:|:--|
| Facebook | [SDK](https://facebook-sdk.readthedocs.io/en/latest/) |
| Instagram | [Developer Library](https://www.instagram.com/developer/libraries/) | 
| YouTube | [Developer Guide](https://developers.google.com/youtube/v3/quickstart/python) | 

### Delivering Data verus Syndromic Surveillance

 Twitter provides varying levels of access depending on how much one can pay. Completely free access provides a 1% random sample of streaming tweets. The sampling methodology is not clear. It is for example not known how long one must weight in between sampling for the two samples to be independent. 
 
  Twitter's approach is not unique. Social media web sites (and their APIs) are meant to let other applications access current data. Sampling is provided to allow devices with low bandwidth to recieve data, not to support statistical inference. 
  
  **Geographic bias** The geographic information over-represents urban areas[^1]. 


[^1]: Hecht, B. and Stephens, M., 2014, May. A tale of cities: Urban biases in volunteered geographic information. In Eighth International AAAI Conference on Weblogs and Social Media.

## Acquiring JSON Data (Day 2)
[Back to Table of Contents](#toc)

1. Streaming versus Historical Data [Twitter package](https://stackabuse.com/accessing-the-twitter-api-with-python/)
2. The `json` package
4. Storage (there's an API for that)
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
