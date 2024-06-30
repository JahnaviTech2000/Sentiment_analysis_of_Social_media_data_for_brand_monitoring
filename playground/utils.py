# import tweepy
# from .models import *

# CONSUMER_KEY = 'FV596ER9iKISaGPHzdf4pbSPV'
# CONSUMER_SECRET = 'xrXg1bnExROpG745dzV4Bkk8bKbdPGkbI85QKuQ8yneQpy6Ogq'
# ACCESS_TOKEN = '1755967459230617600-83erdzrUMap3AdyiNXZBjUytwUza2K'
# ACCESS_TOKEN_SECRET = 'CG6Gi1cejPRVIjyTZMu66xuoamIDNYvG9WxJpspOubaNS'

# auth = tweepy.OAuth1UserHandler(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
# api = tweepy.API(auth)


# def get_tweets_and_comments(username):
#     tweets = api.user_timeline(screen_name=username, count=100)

#     for tweet in tweets:
#         # Save the tweet
#         new_tweet = Tweet.objects.create(tweet_id=tweet.id_str, tweet_text=tweet.text)

#         # Get comments
#         comments = api.search(q=f'to:{username}', since_id=tweet.id, count=100)

#         for comment in comments:
#             print(comment)
#             # Save the comment
#             Comment.objects.create(tweet=new_tweet, comment_text=comment.text)

