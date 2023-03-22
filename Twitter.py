import tweepy
# Creating the authenitcation object
consumer_key = 'QIqgjITOfksfMW4lRLDacQ'
consumer_secret = 'R8x0xN9iSKXGNxUtGKA2hgnlIhh5INZIOdgEfxzk'
access_token = '1401204486-BeLUAuruh294KeJX8NXvdqjCeZOQcLl6HWmMlgA'
access_token_secret = 'pwjiLF42TbORaXtkCS5Oc24qywOU0eFN0esVcibA'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# Setting your acess token and secret
auth.set_access_token(access_token, access_token_secret)
# Creating the API object while passing in auth information
api = tweepy.API(auth)
name = "@Telepeturtle"
# Number of tweets pulled
tweetCount = 10
# Caling the user_timeline function with our parameters
results = api.user_timeline(screen_name=name, count=tweetCount)
print(f"Tweets from {name}: \n")
# for each through all tweets pulled
for tweet in results:
    # printing text stored inside the tweet object
    print(tweet.text)
    print()
