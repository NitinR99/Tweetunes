from google.cloud import language_v1
from google.cloud.language_v1 import enums

import tweepy
from requests_oauthlib import OAuth1Session
from twython import Twython
import requests
from flask import request

twitter = Twython('wzUmqwrgXIaVisMOUrSXv3Hgd', "fa9HgSTQahE3gw0UjUvydnmz2FzpgUkFhTC7RFB7W9YchTUyQb")

auth = twitter.get_authentication_tokens(callback_url='http://tweetunes.space')

OAUTH_TOKEN = auth['oauth_token']
OAUTH_TOKEN_SECRET = auth['oauth_token_secret']

print (auth['auth_url'])

oauth_verifier = request.GET['oauth_verifier']

twitter = Twython("wzUmqwrgXIaVisMOUrSXv3Hgd", "fa9HgSTQahE3gw0UjUvydnmz2FzpgUkFhTC7RFB7W9YchTUyQb",
                  OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

final_step = twitter.get_authorized_tokens(oauth_verifier)

OAUTH_TOKEN = final_step['oauth_token']
OAUTH_TOKEN_SECRET = final_step['oauth_token_secret']


twitter = Twython("wzUmqwrgXIaVisMOUrSXv3Hgd", "fa9HgSTQahE3gw0UjUvydnmz2FzpgUkFhTC7RFB7W9YchTUyQb",
                  OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

print(twitter.get_home_timeline())
sample_analyze_sentiment(twitter.get_home_timeline())

def sample_analyze_sentiment(text_content):
    
    client = language_v1.LanguageServiceClient()

    # Available types: PLAIN_TEXT, HTML
    type_ = enums.Document.Type.PLAIN_TEXT

    # Available values: NONE, UTF8, UTF16, UTF32
    encoding_type = enums.EncodingType.UTF8
    
    language = "en"
    document = {"content": text_content, "type": type_, "language": language}
    
    response = client.analyze_sentiment(document, encoding_type=encoding_type)
    # Get overall sentiment of the input document
    print(u"Document sentiment score: {}".format(response.document_sentiment.score))
    print(u"Document sentiment magnitude: {}".format(response.document_sentiment.magnitude))

'''
# Authenticate to Twitter
auth = tweepy.OAuthHandler("wzUmqwrgXIaVisMOUrSXv3Hgd", "fa9HgSTQahE3gw0UjUvydnmz2FzpgUkFhTC7RFB7W9YchTUyQb")
auth.set_access_token("2654747796-MrlYijOP5CyqaEd1hzc25umNIH8H43WbHzwIsg5", "SkyjIIJnr53GKRoL0bQYGbMXc8kxr2ueiJSpiQ06B7UbA")

# Create API object
api = tweepy.API(auth)

# Create a tweet
#api.update_status("Hello Tweepy")
i=0
for status in tweepy.Cursor(api.user_timeline, screen_name='@realDonaldTrump').items():
    if(i==10):
        break
    sample_analyze_sentiment(status.text)
    i+=1


sample_analyze_sentiment('The stunning remnants of an exploded star include elements that helped build life on Earth')
'''