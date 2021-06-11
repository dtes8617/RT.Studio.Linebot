import datetime

from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

from config import config

# If modifying these scopes, delete the file token.json.
SCOPES = config.google_calendar_scope
TOKEN = config.google_calendar_token


def main():
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's Calendar.
    """
    creds = Credentials.from_authorized_user_info(TOKEN, SCOPES)
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.

    service = build('Calendar', 'v3', credentials=creds)

    # Call the Calendar API
    now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
    print('Getting the upcoming 10 events')
    events_result = service.events().list(calendarId='primary', timeMin=now,
                                          maxResults=10, singleEvents=True,
                                          orderBy='startTime').execute()
    events = events_result.get('items', [])

    if not events:
        print('No upcoming events found.')
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        print(start, event['summary'])


if __name__ == '__main__':
    main()
