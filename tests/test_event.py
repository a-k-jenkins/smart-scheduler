from scheduler.event import Event
from datetime import datetime, timedelta
import pytest


@pytest.fixture(scope="function")
def event_with_defaults():
    return Event("abc", datetime(2025, 1, 29, 18, 30), timedelta(minutes=90))


@pytest.fixture(scope="function")
def event_with_all_fields():
    labels = set({"outdoors", "food"})
    attendees = set({"Jo Mo", "Ana Ono", "Pell Bell"})
    return Event(
        "def",
        datetime(2025, 1, 31, 21, 0),
        timedelta(hours=2),
        labels,
        "a description",
        attendees,
    )


def test_add_attendee(event_with_defaults):
    event_with_defaults.add_attendee("Nadia Fink")
    expected = set({"Nadia Fink"})
    assert event_with_defaults.attendees == expected


def test_add_attendees(event_with_defaults):
    event_with_defaults.add_attendees(["Aristotle", "Anaximander", "Pythagoras"])
    expected = set({"Aristotle", "Anaximander", "Pythagoras"})
    assert event_with_defaults.attendees == expected


def test_remove_attendee_success(event_with_all_fields):
    result = event_with_all_fields.remove_attendee("Jo Mo")
    expected = set({"Ana Ono", "Pell Bell"})
    assert result
    assert event_with_all_fields.attendees == expected


def test_remove_attendees_success(event_with_all_fields):
    result = event_with_all_fields.remove_attendees(["Ana Ono", "Pell Bell"])
    expected = set({"Jo Mo"})
    assert result
    assert event_with_all_fields.attendees == expected


def test_remove_attendees_failure(event_with_all_fields):
    result = event_with_all_fields.remove_attendees(
        ["Ana Ono", "Someone Who Isn't Real"]
    )
    expected = set({"Jo Mo", "Pell Bell"})
    assert not result
    assert event_with_all_fields.attendees == expected
