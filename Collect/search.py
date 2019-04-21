from auth import login
import tweepy
api = tweepy.API(login)


places = api.geo_search(query="calgary", granularity="city")
place_id = places[0].id

tweets = api.search(q="place:%s" % place_id, count=200)
# foreach through all tweets pulled
for tweet in tweets:
    print (tweet)