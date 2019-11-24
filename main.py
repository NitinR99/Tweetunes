from google.cloud import language_v1
from google.cloud.language_v1 import enums
from twython import Twython
from flask import request
import tweepy
import config
import requests


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
    return response.document_sentiment.score, response.document_sentiment.magnitude
        
    
twitter = Twython(config.api_key, config.api_secret)

auth = twitter.get_authentication_tokens(callback_url='http://tweetunes.space')

OAUTH_TOKEN = auth['oauth_token']
OAUTH_TOKEN_SECRET = auth['oauth_token_secret']

print (auth['auth_url'])

oauth_verifier = request.GET['oauth_verifier']

twitter = Twython(config.api_key, config.api_secret,
                  OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

final_step = twitter.get_authorized_tokens(oauth_verifier)

OAUTH_TOKEN = final_step['oauth_token']
OAUTH_TOKEN_SECRET = final_step['oauth_token_secret']


twitter = Twython(config.api_key, config.api_secret,
                  OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

print(twitter.get_home_timeline())
sample_analyze_sentiment(twitter.get_home_timeline())

"""SPOTIFY API"""

endpoint_url = "https://api.spotify.com/v1/recommendations?"

limit = 20
energy = magnitude/5.5
valence = (sentiment + 1)/2

query = f'{endpoint_url}limit={limit}&energy={energy}&valence={valence}'

response =requests.get(query, 
               headers={"Content-Type":"application/json", 
                        "Authorization":"Bearer YOUR_TOKEN_HERE"})



