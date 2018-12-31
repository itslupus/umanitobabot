from src.config import Config
from src.sql import SQL

import praw
import os
import re

config = Config()
sql = SQL()

reddit = praw.Reddit(
    client_id = config.getItem('ACCOUNT', 'CLIENT_ID'),
    client_secret = config.getItem('ACCOUNT', 'CLIENT_SECRET'),
    user_agent = config.getItem('ACCOUNT', 'USER_AGENT'),
    username = config.getItem('ACCOUNT', 'USERNAME'),
    password = config.getItem('ACCOUNT', 'PASSWORD')
)

try:
    for submission in reddit.subreddit('armpit_test').stream.submissions(skip_existing = True):
        # find all that matches ABCD 1234
        matches = re.findall(r'[A-Z]{3} [1-9]{3}', submission.title.upper())
        # find all that matches ABCD1234
        matches.extend(re.findall(r'[A-Z]{3}[1-9]{3}', submission.title.upper()))
        print(matches)
except Exception as e:
    print(e)
    exit()