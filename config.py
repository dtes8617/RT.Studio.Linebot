import json
import os

from dotenv import load_dotenv

load_dotenv()

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    google_calendar_token = json.loads(os.getenv('GOOGLE_CALENDAR_CREDENTIAL'))
    google_calendar_scope = [os.getenv('GOOGLE_CALENDAR_SCOPE')]

    linebot_access_token = os.getenv('LINEBOT_ACCESS_TOKEN')
    linebot_secret = os.getenv('LINEBOT_SECRET')

    log_file_path = os.path.join(basedir, os.getenv('LOG_FILE_PATH'))


config = Config()
