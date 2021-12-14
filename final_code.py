from numpy import place
import pandas as pd
import requests
import tweepy
import time
from datetime import datetime, tzinfo
import json
from pandas.io.json import json_normalize
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import numpy as np
import nltk
import ast
nltk.download('vader_lexicon')

my_headers = {'Authorization' : 'Bearer {}'} #removed token for final submission
first_response = requests.get("https://api.twitter.com/1.1/tweets/search/fullarchive/DevCOP26.json?query=COP26&fromDate=202111110000&toDate=202111180000&maxResults=100", headers=my_headers)
x = first_response.json()
next = x['next']
temp = pd.DataFrame(x['results'])
df = temp[temp.place.notnull()]
#loop through all tweets mentioning COP26 from that week, currently stops at 1000
while next is not None and df.shape[0] < 2300:
    response = requests.get("https://api.twitter.com/1.1/tweets/search/fullarchive/DevCOP26.json?query=COP26&fromDate=202111110000&toDate=202111180000&maxResults=100&next={}".format(next), headers=my_headers)
    if response.status_code == 200:
        temp= response.json()
        temp_df = pd.DataFrame(temp['results'])
        df = df.append(temp_df, ignore_index=True)
        next = temp['next']
    else: #if rate_mit is hit
        time.sleep(300)


df_en = df[df['lang'] == 'en']

sid = SentimentIntensityAnalyzer()
df_en['compound'] = [sid.polarity_scores(x)['compound'] for x in df_en['text']]
df_en['neg'] = [sid.polarity_scores(x)['neg'] for x in df_en['text']]
df_en['neu'] = [sid.polarity_scores(x)['neu'] for x in df_en['text']]
df_en['pos'] = [sid.polarity_scores(x)['pos'] for x in df_en['text']]


copy = df_en.copy(deep=True)

df_neg = copy[copy['compound'] < -.2]
df_pos = copy[copy['compound'] > .2]
df_neu = copy[(copy['compound'] <= .2) & (copy['compound'] >= -.2)]

df_location = df_en[~df_en['user.derived.locations'].isnull()]
df_location['Country_Code'] = None
for index, row in df_location.iterrows():
    a = row['user.derived.locations']
    tmp = ast.literal_eval(a[1:-1])
    df_location['Country_Code'][index] = tmp['country_code']

df.to_excel("social_media_group.xlsx")
df_location.to_excel("social_media_group_location.xlsx")




#####Initially intended on using the above code, we quickly ran into issues with the api request rate limits, below is what we used to build teh dataframe, selecting a small subset from each day
def jsonify_tweepy(tweepy_object):
    json_str = json.dumps(tweepy_object._json)
    return json.loads(json_str)

API_Key = '' #removed for app privacy
API_Key_secret = ''#removed for app privacy
Bearer_token = ''#removed for app privacy
access_token = ''#removed for app privacy
access_token_secret = ''#removed for app privacy

# Authorization to consumer key and consumer secret 
auth = tweepy.OAuthHandler(API_Key, API_Key_secret) 
# Access to user's access key and access secret 
auth.set_access_token(access_token, access_token_secret) 
# Make an instance of the API class. Call it 'api' 
api = tweepy.API(auth, wait_on_rate_limit=True)#, host='https://api.twitter.com/1.1/tweets/search/fullarchive/DevCOP26.json') #, wait_on_rate_limit_notify=True) 


tmp = api.search_full_archive(label='DevCOP26', query="COP26", fromDate=202111110000, toDate=202111111200)
ll = [jsonify_tweepy(i) for i in tmp]
df = pd.json_normalize(ll)

tmp = api.search_full_archive(label='DevCOP26', query="COP26", fromDate=202111111200, toDate=202111120000)
ll = [jsonify_tweepy(i) for i in x]
qq = pd.json_normalize(ll)
df = df.append(qq)


tmp = api.search_full_archive(label='DevCOP26', query="COP26", fromDate=202111120000, toDate=202111121200)
ll = [jsonify_tweepy(i) for i in x]
qq = pd.json_normalize(ll)
df = df.append(qq)

tmp = api.search_full_archive(label='DevCOP26', query="COP26", fromDate=202111121200, toDate=202111130000)
ll = [jsonify_tweepy(i) for i in x]
qq = pd.json_normalize(ll)
df = df.append(qq)

tmp = api.search_full_archive(label='DevCOP26', query="COP26", fromDate=202111130000, toDate=202111131200)
ll = [jsonify_tweepy(i) for i in x]
qq = pd.json_normalize(ll)
df = df.append(qq)

tmp = api.search_full_archive(label='DevCOP26', query="COP26", fromDate=202111131200, toDate=202111140000)
ll = [jsonify_tweepy(i) for i in x]
qq = pd.json_normalize(ll)
df = df.append(qq)

tmp = api.search_full_archive(label='DevCOP26', query="COP26", fromDate=202111140000, toDate=202111141200)
ll = [jsonify_tweepy(i) for i in x]
qq = pd.json_normalize(ll)
df = df.append(qq)

tmp = api.search_full_archive(label='DevCOP26', query="COP26", fromDate=202111141200, toDate=202111150000)
ll = [jsonify_tweepy(i) for i in x]
qq = pd.json_normalize(ll)
df = df.append(qq)

tmp = api.search_full_archive(label='DevCOP26', query="COP26", fromDate=202111150000, toDate=202111151200)
ll = [jsonify_tweepy(i) for i in x]
qq = pd.json_normalize(ll)
df = df.append(qq)

tmp = api.search_full_archive(label='DevCOP26', query="COP26", fromDate=202111151200, toDate=202111160000)
ll = [jsonify_tweepy(i) for i in x]
qq = pd.json_normalize(ll)
df = df.append(qq)

tmp = api.search_full_archive(label='DevCOP26', query="COP26", fromDate=202111160000, toDate=2021111601200)
ll = [jsonify_tweepy(i) for i in x]
qq = pd.json_normalize(ll)
df = df.append(qq)

tmp = api.search_full_archive(label='DevCOP26', query="COP26", fromDate=202111161200, toDate=202111170000)
ll = [jsonify_tweepy(i) for i in x]
qq = pd.json_normalize(ll)
df = df.append(qq)

tmp = api.search_full_archive(label='DevCOP26', query="COP26", fromDate=202111170000, toDate=202111171200)
ll = [jsonify_tweepy(i) for i in x]
qq = pd.json_normalize(ll)
df = df.append(qq)

tmp = api.search_full_archive(label='DevCOP26', query="COP26", fromDate=202111171200, toDate=202111180000)
ll = [jsonify_tweepy(i) for i in x]
qq = pd.json_normalize(ll)
df = df.append(qq)

tmp = api.search_full_archive(label='DevCOP26', query="COP26", fromDate=202111180000, toDate=202111181200)
ll = [jsonify_tweepy(i) for i in x]
qq = pd.json_normalize(ll)
df = df.append(qq)

tmp = api.search_full_archive(label='DevCOP26', query="COP26", fromDate=202111181200, toDate=202111190000)
ll = [jsonify_tweepy(i) for i in x]
qq = pd.json_normalize(ll)
df = df.append(qq)

tmp = api.search_full_archive(label='DevCOP26', query="COP26", fromDate=202111190000, toDate=202111191200)
ll = [jsonify_tweepy(i) for i in x]
qq = pd.json_normalize(ll)
df = df.append(qq)

tmp = api.search_full_archive(label='DevCOP26', query="COP26", fromDate=202111191200, toDate=202111200000)
ll = [jsonify_tweepy(i) for i in x]
qq = pd.json_normalize(ll)
df = df.append(qq)

tmp = api.search_full_archive(label='DevCOP26', query="COP26", fromDate=202111200000, toDate=202111201200)
ll = [jsonify_tweepy(i) for i in x]
qq = pd.json_normalize(ll)
df = df.append(qq) 
