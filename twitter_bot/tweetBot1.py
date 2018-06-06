import tweepy
from time import sleep

consumer_key = 'iom1IEMhR0Kr4Q2PZpWfCEciL'
consumer_secret = '7h4yUkAHErmSilG7daSQlJFqLwmM1QUMGCODRw0UfkjKbXscG3'
access_token = '823450711035965441-kN5nISH2E7xppK0vghzHHkfEwWnSDVC'
access_token_secret = '7RmlYM6ON8GiQ7lOIolJ8vVXuW1jY9iL331tXAlI9eNnf'

auth =  tweepy.OAuthHandler(consumer_key, consumer_secret)

auth.set_access_token(access_token, access_token_secret)

auth.secure = True

api =  tweepy.API(auth)

myBot = api.get_user(screen_name = '@Idan244')

api.create_list(name="Sorry for adding you", mode="public", description="I had to add you sorry:(")

for tweet in tweepy.Cursor(api.search,q='#Purim',lang='he').items(10):
    try:

        if tweet.user.id == myBot.id:
            continue

        print("\n\nFound tweet by: @" + tweet.user.screen_name)

        if(tweet.retweeted == False) or (tweet.favorited == False):
            tweet.retweet()
            tweet.favorite()
            print("Retweeted and favorited the tweet")

        if tweet.user.following == False:
            tweet.user.follow()
            print("Followed the user")




    except tweepy.TweepError as e:
        print(e.reason)
        sleep(10)
        continue

    except StopIteration:
        break
