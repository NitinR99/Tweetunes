from twython import Twython
from flask import request
import os

twitter = Twython(os.environ.get('CONSUMER_KEY'), os.environ.get('CONSUMER_SECRET'))

auth = twitter.get_authentication_tokens(callback_url='https://oauth.io/auth')

OAUTH_TOKEN = auth['oauth_token']
OAUTH_TOKEN_SECRET = auth['oauth_token_secret']

oauth_verifier = request.GET['oauth_verifier']

twitter = Twython(os.environ.get('CONSUMER_KEY'), os.environ.get('CONSUMER_SECRET'),
                  OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

final_step = twitter.get_authorized_tokens(oauth_verifier)

OAUTH_TOKEN = final_step['oauth_token']
OAUTH_TOKEN_SECRET = final_step['oauth_token_secret']

twitter = Twython(os.environ.get('CONSUMER_KEY'), os.environ.get('CONSUMER_SECRET'),
                  OAUTH_TOKEN, OAUTH_TOKEN_SECRET)


def get_timeline():
    return twitter.get_home_timeline()
