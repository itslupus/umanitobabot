import configparser
import os

class Config:
    path = os.path.dirname(os.path.realpath(__file__))

    def __init__(self):
        self.config = configparser.ConfigParser()
        # check if a config.ini file exists
        if (not os.path.isfile(self.path + '/../config.ini')):
            self.createConfig()
        
        self.config.read(self.path + '/../config.ini')

    def createConfig(self):
        self.config['ACCOUNT'] = {}
        self.config['ACCOUNT']['CLIENT_ID'] = 'id'
        self.config['ACCOUNT']['CLIENT_SECRET'] = 'secret'
        self.config['ACCOUNT']['USER_AGENT'] = 'script:umanitobabot:v0.1[dev] (by /u/_Armpit)'
        self.config['ACCOUNT']['USERNAME'] = 'usrname'
        self.config['ACCOUNT']['PASSWORD'] = 'passwrd'

        try:
            with open(self.path + '/../config.ini', 'w') as file:
                self.config.write(file)
        except Exception as e:
            print(e)
            exit()

    def getItem(self, catagory, item):
        if (not os.path.isfile(self.path + '/../config.ini')):
            self.createConfig()

        return self.config[catagory][item]