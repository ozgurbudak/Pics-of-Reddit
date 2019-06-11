from urllib import request

import praw
from prawcore import NotFound
import datetime as dt
import os
import json
import tweepy
import time
from tweepy import OAuthHandler



consumer_key = '***********************************'
consumer_secret = '***********************************'
access_token = '***********************************'
access_token_secret = '***********************************'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
 
#api = tweepy.API(auth)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, retry_count=3, retry_delay=60)







reddit = praw.Reddit(client_id='***********************************', \
                     client_secret='***********************************', \
                     user_agent='***********************************', \
                     username='***********************************', \
                     password='***********************************')



subreddit_list= "1000words+analog+AnythingYouCanTakeAPhotographOfPorn+askphotography+AsKPhotography+astrophotography+beerporn+Cameraporn+cameras+catpictures+ChicagoPics+CoolPics+Decade+EarthPorn+fashionphotography+filmphotography+foodshots+FrostingPorn+GreatPics+hdr+headshots+imgur+leica+lightroom+lomography+LondonPics+m43+nex+Pentax+photoassignments+Photoessay+photographers+photographic+Photography+PhotoIt+photojournalism+photos+photoshop+pics+pics2+picss+portraitphotos+portraits+postprocessing+ProPhotoTips+ratemypic+raweddits+redditor_pics+RedditorsInAction+shittyHDR+shutterbugs+ToyCamera+Unbelievable+urbanexploration+video+weedpics+whatcamerashouldibuy"
subreddit = reddit.subreddit(subreddit_list)
i=0
for submission in subreddit.top(limit=100,time_filter="day"):
    if i==10:
        break
    else:
        urlOfPic= "https://proxy.duckduckgo.com/iu/?u=" + submission.url
        titleOfPic= submission.title
        f = open('{}.jpg'.format(i), 'wb')
        f.write(request.urlopen(urlOfPic).read())
        f.close()
        if (os.stat('{}.jpg'.format(i)).st_size < (3072 * 1024)) and urlOfPic[len(urlOfPic)-4]=='.':
            print(urlOfPic)
            api.update_with_media('{}.jpg'.format(i), titleOfPic)
            print("done")
            os.remove('{}.jpg'.format(i))
            i=i+1
        
        
