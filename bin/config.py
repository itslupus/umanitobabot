import configparser
import os

class Config:
    def __init__():
        # check if a config.ini file exists
        self.config = configparser.ConfigParser()
        if (not os.path.isfile('../config.ini')):
            self.initConfig()

        self.config.read(workingDir + '/config.ini')

    def initConfig():
        self.config['ACCOUNT'] = {}
            self.config['ACCOUNT']['CLIENT_ID'] = 'id'
            self.config['ACCOUNT']['CLIENT_SECRET'] = 'secret'
            self.config['ACCOUNT']['USER_AGENT'] = 'script:umanitoba_bot:v0.1[dev] (by /u/_Armpit)'
            self.config['ACCOUNT']['USERNAME'] = 'usrname'
            self.config['ACCOUNT']['PASSWORD'] = 'passwrd'

            try:
                with open('../config.ini', 'w') as file:
                    self.config.write(file)
            except Exception as e:
                print(e)
                exit()

    def getItem(catagory, item):
        if (not os.path.isfile('../config.ini')):
            self.initConfig()

        return self.config[str(catagory).upper][str(item).upper]