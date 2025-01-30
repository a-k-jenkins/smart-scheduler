from scheduler.event import Event
from datetime import datetime, timedelta


def test_event():
    event = Event("abc", datetime(2025, 1, 29, 18, 30), timedelta(minutes=90))
    print(event)
