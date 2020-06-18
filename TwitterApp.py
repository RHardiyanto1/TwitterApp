import twitter
import os

consumer_key = os.environ['consumer_key']
consumer_secret = os.environ['consumer_secret']
access_token = os.environ['access_token']
access_token_secret = os.environ['access_token_secret']

auth = twitter.OAuth(access_token, access_token_secret,
                     consumer_key, consumer_secret)
t = twitter.Twitter(auth=auth)

# Functions
def update_status(update):
    t.statuses.update(status=update)

def get_home_timeline():
    t.statuses.home_timeline()

def send_direct_message(user, message):
    t.direct_message.new(user, message)

