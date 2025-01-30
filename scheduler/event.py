from datetime import datetime, timedelta


class Event:
    """
    class for a single event. Every event must have:
        - name
        - start_time (datetime)
        - duration (timedelta)
    Optional:
        - labels (set)
        - description
        - attendees (set)
    """

    def __init__(
        self,
        name: str,
        start_time: datetime,
        duration: timedelta,
        labels: set = set(),
        description: str = "",
        attendees: set = set(),
    ):
        Event.__validate_inputs(
            name, start_time, duration, labels, description, attendees
        )
        self.name = name
        self.start_time = start_time
        self.labels = labels
        self.description = description
        self.attendees = attendees

    def __repr__(self):
        print(
            f'Event("{self.name}", "{self.start_time}", "{str(self.labels)}", "{self.description}", "{str(self.attendees)}")'
        )

    def __str__(self):
        s = f"""
        Event:
        \tName:        {self.name}
        \tTime:        {self.start_time}
        \tLabels:      {self.labels}
        \tDescription: {self.description}
        \tAttendees:   {self.attendees}
        """

        return s

    @staticmethod
    def __validate_inputs(name, start_time, duration, labels, description, attendees):
        assert len(name) <= 25  # arbitrary
        assert len(labels) <= 10
        assert len(description) <= 500

    def add_attendee(self, attendee_id):
        self.attendees.append(attendee_id)

    def change_time(self, new_time=None, new_duration=None):
        if new_time:
            self.start_time = new_time
        if new_duration:
            self.duration = new_duration


e = Event("my_name", datetime(2024, 1, 7, 15, 16), timedelta(30))
print(e)
