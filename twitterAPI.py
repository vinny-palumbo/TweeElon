'''
Using the Twitter API:
https://developer.twitter.com/en/docs/twitter-api/getting-started/guide
'''


import os
import requests
import json

import config

# set twitter API environment variables
os.environ["CONSUMER_KEY"]= config.params["CONSUMER_KEY"]
os.environ["CONSUMER_SECRET"]= config.params["CONSUMER_SECRET"]
os.environ["BEARER_TOKEN"]= config.params["BEARER_TOKEN"]

class TwitterAPI():
    
    def __init__(self, author, word):
        self.AUTHOR_ID = author
        self.TARGET_WORD = word
    
    def auth(self):
        return os.environ.get("BEARER_TOKEN")


    def create_url(self):
        '''
        GET /2/tweets/search/recent: https://developer.twitter.com/en/docs/twitter-api/tweets/search/api-reference/get-tweets-search-recent
        
        Building queries for Search Tweets: https://developer.twitter.com/en/docs/twitter-api/tweets/search/integrate/build-a-query
        '''
        query = "from:" + self.AUTHOR_ID
        
        # Tweet fields are adjustable.
        tweet_fields = "tweet.fields=created_at,text"
        
        # build API query
        url = "https://api.twitter.com/2/tweets/search/recent?query={}&{}".format(
            query, tweet_fields
        )
        return url


    def create_headers(self, bearer_token):
        headers = {"Authorization": "Bearer {}".format(bearer_token)}
        return headers


    def connect_to_endpoint(self, url, headers):
        response = requests.request("GET", url, headers=headers)
        if response.status_code != 200:
            raise Exception(response.status_code, response.text)
        return response.json()


    def get_last_tweet_if_word(self, is_test=False):
        bearer_token = self.auth()
        url = self.create_url()
        headers = self.create_headers(bearer_token)
        json_response = self.connect_to_endpoint(url, headers)
        
        if is_test:
            # if testing, print last 10 tweets in console
            result_str = json.dumps(json_response, indent=4, sort_keys=True)
            print(result_str)
        
        # get last tweet text
        last_tweet_info = json_response["data"][0]
        last_tweet_text = last_tweet_info["text"]
        last_tweet_text = last_tweet_text.replace('&amp;','&')
        
        # if target word in last tweet, return it
        if self.TARGET_WORD.lower() in last_tweet_text.lower().split():
            return last_tweet_text
        else:
            return None
        
            
    
def main():
    AUTHOR_ID = "44196397" # Elon's twitter ID
    TARGET_WORD = "#bitcoin"
    tw = TwitterAPI(AUTHOR_ID, TARGET_WORD)
    tweet_with_word = tw.get_last_tweet_if_word(is_test=True)
    
    if tweet_with_word:
        # print last tweet in console
        tweet_with_word_no_unicode = tweet_with_word.encode("ascii", "ignore").decode()
        print(tweet_with_word_no_unicode)

if __name__ == "__main__":
    main()