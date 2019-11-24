from google.cloud import language_v1
from google.cloud.language_v1 import enums
from twython import Twython
from flask import request
import tweepy
import config


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
    

def sample_classify_text(text_content):
    """
    Classifying Content in a String

    Args:

      text_content The text content to analyze. Must include at least 20 words.
    """

    client = language_v1.LanguageServiceClient()

    # text_content = 'That actor on TV makes movies in Hollywood and also stars in a variety of popular new TV shows.'

    # Available types: PLAIN_TEXT, HTML
    type_ = enums.Document.Type.PLAIN_TEXT

    # Optional. If not specified, the language is automatically detected.
    # For list of supported languages:
    # https://cloud.google.com/natural-language/docs/languages
    language = "en"
    document = {"content": text_content, "type": type_, "language": language}

    response = client.classify_text(document)
    # Loop through classified categories returned from the API
    for category in response.categories:
        # Get the name of the category representing the document.
        # See the predefined taxonomy of categories:
        # https://cloud.google.com/natural-language/docs/categories
        print(u"Category name: {}".format(category.name))
        # Get the confidence. Number representing how certain the classifier
        # is that this category represents the provided text.
        print(u"Confidence: {}".format(category.confidence))

    
    
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

