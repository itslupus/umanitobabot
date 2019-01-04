from src.config import Config
from src.sql import SQL

from src import webscrape

import praw
import os
import re
import time

# setup config file and SQL
config = Config()
sql = SQL()

# create reddit instance
reddit = praw.Reddit(
    client_id = config.getItem('ACCOUNT', 'CLIENT_ID'),
    client_secret = config.getItem('ACCOUNT', 'CLIENT_SECRET'),
    user_agent = config.getItem('ACCOUNT', 'USER_AGENT'),
    username = config.getItem('ACCOUNT', 'USERNAME'),
    password = config.getItem('ACCOUNT', 'PASSWORD')
)

def findCourses(string):
    # [A-Z]{4}  match a 4 character string from A to Z
    # ' '?      match space or no space
    # [0-9]{4}  match 4 digit number from 0 to 9
    matches = re.findall(r'[A-Z]{4} ?[0-9]{4}', string.upper())

    return matches

# https://www.reddit.com/r/redditdev/comments/7jng5a/whats_the_best_way_to_monitorreply_to_comments/dr7qn4p/
# solution to having a stream of comments and submissions
def submissions_and_comments(subreddit, **kwargs):
    # create array of comments and submissions
    results = []
    results.extend(subreddit.new(**kwargs))
    results.extend(subreddit.comments(**kwargs))
    results.sort(key = lambda post: post.created_utc, reverse = True)

    return results

'''
# continous stream, anything past this is included in the loop
stream = praw.models.util.stream_generator(lambda **kwargs: submissions_and_comments(reddit.subreddit('armpit_test'), **kwargs), skip_existing = False)
for new in stream:
    content = None

    if (type(new) is praw.models.Submission):
        content = new.title + ' ' + new.selftext
    elif (type(new) is praw.models.Comment):
        content = new.body

    courses = findCourses(content)

    for course in courses:
        courseSplit = course.split()
        info = webscrape.getAuroraCourse(courseSplit[0], courseSplit[1])
''' and None


result = webscrape.getAuroraCourse('COMP', '2140')
print(result)

'''
get = sql.getCourseInfo('COMP', '2140')

if (get != None):
    t = time.time()
    
    if (get['last_update'] + (60 * 1) < t):
        result = webscrape.getAuroraCourse('COMP', '2140')
        sql.updateCourseInfo(get['id'], result['title'], result['desc'], result['notHeld'], result['preReq'])
else:
    result = webscrape.getAuroraCourse('COMP', '2140')
    sql.insertCourseInfo('COMP', 2140, result['title'], result['desc'], result['notHeld'], result['preReq'])
''' and None