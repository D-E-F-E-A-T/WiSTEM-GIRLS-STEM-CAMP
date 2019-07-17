import tweepy
import schedule
import time

consumer_key = ""
consumer_secret = ""
access_token = ""
accesss_token_secret = ""

#Settings up Tweepy

#tweets = twitter_api.home_timeline()

def post_tweet(tweet):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    twitter_api = tweepy.API(auth)
    
    twitter_api.update_status(tweet)
    
    print ("Tweet Posted")