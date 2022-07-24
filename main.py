from array import array
import tweepy
from time import sleep
from decouple import config

CONSUMER_KEY = config('CONSUMER_KEY')
CONSUMER_SECRET = config('CONSUMER_SECRET')
ACCESS_TOKEN = config('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = config('ACCESS_TOKEN_SECRET')

# ID of @learnwithsob account
BOT_ID = 1550810447947132928
SLEEP_TIME = 125


# Twitter authentication
def api():
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    return tweepy.API(auth)

def retweet(tweepy_api: tweepy.API, hashtag:str, delay=SLEEP_TIME, items=10):
    for tweet in tweepy.Cursor(tweepy_api.search, q=hashtag).items(items):

        try:
            tweet_id = dict(tweet._json)['id']

            tweepy_api.retweet(tweet_id)
            tweepy_api.create_favorite(tweet_id)

        except tweepy.TweepError as error:
            print(error)
            sleep(1)

    sleep(delay)



if __name__ == '__main__':
    api = api()

    while True:
        retweet(api, '@summerofbitcoin', delay=5, items=3)
        retweet(api, '#summerofbitcoin', delay=5, items=3)
        
        retweet(api, '#LightningNetwork', delay=5, items=3)
        retweet(api, '#Bitcoin', delay=5, items=3)
        
        # Sponsors
        retweet(api, '@spiralbtc', delay=5, items=3)
        retweet(api, '@coinbase', delay=5, items=3)
        retweet(api, '@CathedraBitcoin', delay=5, items=3)
        retweet(api, '@MarathonDH', delay=5, items=3)
        retweet(api, '@superlunarhq', delay=5, items=3)
        retweet(api, '@NYDIG_BTC', delay=5, items=3)
        retweet(api, '@HRF', delay=5, items=3)
        retweet(api, '@unchainedcap', delay=5, items=3)
        retweet(api, '@FutureBit', delay=5, items=3)
        retweet(api, '@BitcoinerJobs', delay=5, items=3)
        retweet(api, '@interview_bit', delay=5, items=3)
        retweet(api, '@Ledger', delay=5, items=3)

        # Special
        retweet(api, '@jack', delay=5, items=3)
        retweet(api, '@halfin', delay=5, items=3)

        # Projects
        retweet(api, '@eyeofsatoshi', delay=5, items=3)
        retweet(api, '@lightning', delay=5, items=3)
        retweet(api, '@bitcoindevkit', delay=5, items=3)
        retweet(api, '@MagicalBitcoin', delay=5, items=3)
        retweet(api, '@HexaWallet', delay=5, items=3)
        retweet(api, '@ZeusLN', delay=5, items=3)
        retweet(api, '@Suredbits', delay=5, items=3)
        retweet(api, '@Bcoin', delay=5, items=3)
        retweet(api, '@getAlby', delay=5, items=3)
        retweet(api, '@Breez_Tech', delay=5, items=3)
        retweet(api, '@GaloyMoney', delay=5, items=3)
        
        
