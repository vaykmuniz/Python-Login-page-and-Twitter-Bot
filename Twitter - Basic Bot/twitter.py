from textblob import TextBlob
from pprint import pprint 
import time
import tweepy
import sys 

api_key = ""
api_secret_key = ""
access_token = ""
access_secret_token = ""

auth_handler = tweepy.OAuthHandler(consumer_key=api_key, consumer_secret=api_secret_key)
auth_handler.set_access_token(access_token, access_secret_token)

api = tweepy.API(auth_handler)

alvo = "GahMuniz_" #Bot Target
usuario = api.get_user(alvo)
user_tl = api.user_timeline(screen_name=usuario.screen_name, count=1)
for tweets in user_tl:
    t_atual = tweets.id
    print(tweets.text, tweets.id, tweets.user.screen_name)

while True:
    hehe = api.user_timeline(screen_name = usuario.screen_name, since_id = t_atual, count = 1)
    if hehe == []:
        print("Nothing New")
        time.sleep(20)
    else:
        try:
            t_atual=hehe[0].id
            api.create_favorite(id = t_atual)
            api.update_status(status=f'@{usuario.screen_name} Nice Stuff!', in_reply_to_status_id=t_atual)
            print("Faved and Commented :)")
        except:
            print('Bug - Tweet may have been deleted')
