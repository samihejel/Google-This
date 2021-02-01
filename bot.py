import praw
import time
from googlesearch import search


subredditName = 'bigmodeisland'
user = 'thenicestbot'
password = 'thenicestbot'
secret = 'SrZYun3-q25POYKFQ3SMGElXj08mUA'
clientID = 'vvQ5ZJy61TBMxA'
reddit = praw.Reddit(client_id=clientID,
                     user_agent ='thegooglebot',
                     client_secret= secret,
                     username= user,
                     password= password)
subreddit = reddit.subreddit(subredditName)

key = '!googleThis'

for comment in subreddit.stream.comments():
    if key in comment.body:
        reply ='Hi! I\'ve gathered the first 10 google results for your search, here they are!  \n'
        print('hi')
        searchquery = comment.body.replace(key, '')
        if searchquery != '':
            searchList = search(searchquery)
            for link in searchList:
                reply += link + '  \n'
            comment.reply(reply) 
        print('commented')
        time.sleep(4)