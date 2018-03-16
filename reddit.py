import praw
import config
import time

def bot_login():
    print("Logging in")
    tmp = praw.Reddit(username = config.username,
                password = config.password,
                client_id = config.client_id,
                client_secret = config.client_secret,
                user_agent = "reddit test bot v0.1")
    print("logged in")

    return tmp

def run_bot(r):
    print("retrieving 25 comments")
    for comment in r.subreddit('dog').comments(limit=10):
        print(comment.body)
        print("scanning comments for 'dog'")
        if "dog" in comment.body and comment.id and comment.author != r.user.me():
            print("string found in " + comment.id)
            comment.reply("Dogs!? Where!?")
            print("sleeping for 600 seconds")
            time.sleep(10)
            print("Replied to a comment" + comment.id)

    print("sleeping for 600 seconds")
    time.sleep(10)

while True:
    r = bot_login()
    run_bot(r)
