import tweepy
import time

from past.builtins import execfile

consumer_key = '6ncaT6Si50JDTpcls3PXDVRMJ'
consumer_secret = '4Qsj4rx6CG5tWiNHubwMHwHCjmjMKCDH6VohRnO724nMOylmeY'
access_token = '1272756484678529030-9Muq65EG4ArPQ3HQneYGhuDIKQjTMl'
access_token_secret = 'rdAfmSItA6VvDGkcTtBl1VXDgtz7znE8QclTYbsoql1B4'
FILE_PATH = 'gen-queue.txt'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

queue_text = []


def generate_new():
    execfile("generate.py")
    with open(FILE_PATH, "r") as queue:
        text = queue.read()
        global queue_text
        queue_text = text.split("%")


def post():
    if len(queue_text) == 0:
        generate_new()
    print(queue_text[0])
    queue_text.pop(0)
    print(queue_text)
    # api.update_status()


while True:
    post()
    time.sleep(10)
