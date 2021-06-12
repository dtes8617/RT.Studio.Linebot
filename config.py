import json
import os
from configparser import ConfigParser

basedir = os.path.abspath(os.path.dirname(__file__))
config_path = os.path.join(basedir, 'config.ini')

config_parser = ConfigParser()
config_parser.read(config_path)


class Config:
    google_calendar_token = json.loads(config_parser.get('google-calendar', 'google_calendar_credential'))
    google_calendar_scope = [config_parser.get('google-calendar', 'google_calendar_scope')]

    linebot_access_token = config_parser.get('line-bot', 'linebot_access_token')
    linebot_secret = config_parser.get('line-bot', 'linebot_secret')

    log_file_path = os.path.join(basedir, config_parser.get('default', 'log_file_path'))


config = Config()
