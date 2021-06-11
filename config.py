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


config = Config()
