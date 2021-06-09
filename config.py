from configparser import ConfigParser

config_parser = ConfigParser()
config_parser.read('config.ini')


class Config:
    google_calendar_username = config_parser.get('google calendar', 'AccountID')


config = Config()