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

    # get all the courses and seperate sub and number (COMP2160 -> COMP 2160)
    for key, value in enumerate(matches):
        if (len(matches[key].split()) != 2):
            matches[key] = ' '.join(value[i:i + 4] for i in range(0,len(value), 4))

    return matches

def log(logType, message):
    # store time and prepare log message
    t = time.gmtime()
    output = f'[{t.tm_year}-{t.tm_mon}-{t.tm_mday} {t.tm_hour}:{t.tm_min}:{t.tm_sec}][{logType}] {message}'

    # open log file for writing (append)
    f = open('f.log', 'a')

    # write log and print
    f.write(output + '\n')
    print(output)

    # clean up our toys
    f.close()

# https://www.reddit.com/r/redditdev/comments/7jng5a/whats_the_best_way_to_monitorreply_to_comments/dr7qn4p/
# solution from another user to having a stream of comments and submissions
def customStream(subreddit, **kwargs):
    # create array of comments and submissions
    results = []
    results.extend(subreddit.new(**kwargs))
    results.extend(subreddit.comments(**kwargs))
    results.sort(key = lambda post: post.created_utc, reverse = True)

    return results

# continous stream, anything in this is included in the loop
def __run__():
    doReply = False

    stream = praw.models.util.stream_generator(lambda **kwargs: submissions_and_comments(reddit.subreddit('armpit_test'), **kwargs), skip_existing = True)
    for new in stream:
        content = None

        if (type(new) is praw.models.Submission):
            content = new.title + ' ' + new.selftext
            log('READ', 'Reading submission ' + str(new))
        elif (type(new) is praw.models.Comment):
            # TODO find comments with [ABCD 1234]
            #content = new.body
            log('READ', 'Reading comment ' + str(new))
            content = None

        if (content != None):
            courses = findCourses(content)
            replyCourseInfo = []

            for course in courses:
                courseSplit = course.split()

                result = webscrape.getAuroraCourse(courseSplit[0], courseSplit[1])
                if (result == None):
                    continue

                doReply = True

                get = sql.getCourseInfo(courseSplit[0], courseSplit[1])

                if (get != None):
                    if (get['last_update'] + (60 * 1) < time.time()):
                        sql.updateCourseInfo(get['id'], result['title'], result['desc'], result['notHeld'], result['preReq'])
                        replyCourseInfo.append((result['title'], result['desc'], result['notHeld'], result['preReq']))
                    else:
                        replyCourseInfo.append((get['title'], get['desc'], get['notHeld'], get['preReq']))
                else:
                    sql.insertCourseInfo(courseSplit[0], courseSplit[1], result['title'], result['desc'], result['notHeld'], result['preReq'])
                    replyCourseInfo.append((result['title'], result['desc'], result['notHeld'], result['preReq']))
                    
            if (doReply):
                log('REPLY', 'Replying to ' + str(new))

                doReply = False
                
                replyStr = ''

                for courseInfo in replyCourseInfo:
                    replyStr = replyStr + '\n' + courseInfo[0] + '|' + courseInfo[1] + '|' + courseInfo[2] + '|' + courseInfo[3]

                new.reply('Course|Description|Not Held With|Prerequisite(s)\n-|-|-|-' + replyStr)

__run__()