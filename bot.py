import praw
import os
import re
import configparser

# less typing for me
workingDir = os.path.dirname(os.path.realpath(__file__))

# check if a config.ini file exists
config = configparser.ConfigParser()
if (not os.path.isfile(workingDir + '/config.ini')):
    config['ACCOUNT'] = {}
    config['ACCOUNT']['CLIENT_ID'] = 'id'
    config['ACCOUNT']['CLIENT_SECRET'] = 'secret'
    config['ACCOUNT']['USER_AGENT'] = 'script:umanitoba_bot:v0.1[dev] (by /u/_Armpit)'
    config['ACCOUNT']['USERNAME'] = 'usrname'
    config['ACCOUNT']['PASSWORD'] = 'passwrd'

    try:
        with open(workingDir + '/config.ini', 'w') as file:
            config.write(file)
    except Exception as e:
        print(e)
        exit()

# read the config file and create a reddit instance
# TODO: should probably check if the config file is actually set
config.read(workingDir + '/config.ini')
reddit = praw.Reddit(
    client_id = config['ACCOUNT']['CLIENT_ID'],
    client_secret = config['ACCOUNT']['CLIENT_SECRET'],
    user_agent = config['ACCOUNT']['USER_AGENT'],
    username = config['ACCOUNT']['USERNAME'],
    password = config['ACCOUNT']['PASSWORD']
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