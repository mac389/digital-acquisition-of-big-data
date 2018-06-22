import json, os 

filename = os.path.join('.','twitter_output.json')
data = json.load(open(filename,'r'))

type(data[0]) #unicode
x = json.loads(data[0]) #convert string to dict

def has_geographic_information(tweet_as_dict, 
        fields_with_geo_information=["geo","place","coordinates"]):
    '''
    print(type(tweet_as_dict))
    print(tweet_as_dict["geo"])
    print(tweet_as_dict["place"])
    print(tweet_as_dict["coordinates"])
    '''
    return bool(tweet_as_dict["geo"]) & bool(tweet_as_dict["place"]) & bool(tweet_as_dict["coordinates"])

geo_counter = 0 
no_geo_counter = 0
for tweet in data:
    if has_geographic_information(json.loads(tweet)):
        geo_counter +=1
    else:
        no_geo_counter +=1

assert (geo_counter + no_geo_counter == len(data))

    '''
    return all([tweet_as_dict["geo"],tweet_as_dict["place"],
                tweet_as_dict["coordinates"]])
    
    return all([tweet_as_dict[field] 
                        for field in fields_with_geo_information])
    '''

'''    
lst = []
for field in fields_with_geo_information:
    list += tweet_as_dict[field]

x.keys()
print(x["text"])
print(x["retweet_count"])
print(x["created_at"])
print(x["coordinates"])
print(x["geo"])
print(x["place"])
print(x["metadata"])
print(x["lang"])
'''