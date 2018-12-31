import configparser
import os

config = configparser.ConfigParser()

def initConfig():
    # check if a config.ini file exists
    if (not os.path.isfile('../config.ini')):
        createConfig()
        config.read(workingDir + '/config.ini')

def createConfig():
    config['ACCOUNT'] = {}
    config['ACCOUNT']['CLIENT_ID'] = 'id'
    config['ACCOUNT']['CLIENT_SECRET'] = 'secret'
    config['ACCOUNT']['USER_AGENT'] = 'script:umanitoba_bot:v0.1[dev] (by /u/_Armpit)'
    config['ACCOUNT']['USERNAME'] = 'usrname'
    config['ACCOUNT']['PASSWORD'] = 'passwrd'

    try:
        with open('../config.ini', 'w') as file:
            config.write(file)
    except Exception as e:
        print(e)
        exit()

def getItem(catagory, item):
    if (not os.path.isfile('../config.ini')):
        createConfig()

    return config[str(catagory).upper][str(item).upper]