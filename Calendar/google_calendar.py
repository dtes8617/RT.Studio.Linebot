from datetime import datetime, timedelta

import pandas as pd
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

import log
from config import config

SCOPES = config.google_calendar_scope
TOKEN = config.google_calendar_token


class CalendarHandler:
    def __init__(self):
        self.creds = None
        self.service = None

    def connect_to_server(self, token: dict = TOKEN, scopes: list = SCOPES):
        self.creds = creds = Credentials.from_authorized_user_info(token, scopes)
        self.service = build('Calendar', 'v3', credentials=creds)
        log.info('Connected to Google Calendar api.')

    def extract_events(self, eventBeginStartTime: datetime = None, eventLastStartTime: datetime = None) -> pd.DataFrame:
        service = self.service

        if not eventBeginStartTime:
            eventBeginStartTime = datetime.now() \
                .replace(hour=23, minute=59, second=59, microsecond=999999)

        eventBeginStartTime = eventBeginStartTime.astimezone().isoformat()

        if not eventLastStartTime:
            eventLastStartTime = (datetime.now() + timedelta(days=2)) \
                .replace(hour=0, minute=0, second=0, microsecond=0)

        eventLastStartTime = eventLastStartTime.astimezone().isoformat()

        events_result = service.events().list(calendarId='primary',
                                              timeMin=eventBeginStartTime,
                                              timeMax=eventLastStartTime,
                                              singleEvents=True,
                                              orderBy='startTime').execute()

        events = events_result.get('items', [])
        events_df = pd.DataFrame(events)

        return events_df
