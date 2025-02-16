from datetime import datetime, timedelta


class Event:
    """class for a single event. Every event must have:
        - name (str)
        - start_time (datetime)
        - duration (timedelta)
    Optional:
        - labels (set)
        - description (str)
        - attendees (set)
    """

    def __init__(
        self,
        name: str,
        start_time: datetime,
        duration: timedelta,
        labels: set[str] = set(),
        description: str = "",
        attendees: set[str] = set(),
    ):
        Event.__validate_inputs(
            name, start_time, duration, labels, description, attendees
        )
        self.name = name
        self.start_time = start_time
        self.labels = labels or set()
        self.description = description or ""
        self.attendees = attendees or set()

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
        assert len(labels) <= 10  # arbitrary
        assert len(description) <= 500  # arbitrary

    def add_attendee(self, attendee: str):
        """Adds attendee name to set of attendees.

        params:
            str: The attendee to add.
        """
        self.attendees.add(attendee)

    def add_attendees(self, attendees: list[str]):
        """Adds multiple attendee names to set of attendees.

        params:
            list[str]: The attendees to add.
        """
        for attendee in attendees:
            self.add_attendee(attendee)

    def remove_attendee(self, attendee: str):
        """Removes attendee from the set of attendees.

        params:
            str: The attendee to remove.
        returns:
            bool: Whether or not the item was successfully removed.
                  "False" if the item was not in the set.
        """
        try:
            self.attendees.remove(attendee)
        except KeyError as e:
            print(f"Failed to remove attendee {attendee} from {self.attendees}")
            return False
        return True

    def remove_attendees(self, attendees: list[str]):
        """Removes attendee from the set of attendees.

        params:
            list[str]: The list of attendees to remove.
        returns:
            bool: Whether or not the items were successfully removed.
                  "False" if any item was not in the set.
        """
        result = True
        for attendee in attendees:
            result = result and self.remove_attendee(attendee)
        return result

    def add_label(self, label: str):
        """Adds label to set of labels.

        params:
            str: The label to add.
        """
        self.labels.add(label)

    def add_labels(self, labels: list[str]):
        """Adds multiple labels to set of labels.

        params:
            list[str]: The labels to add.
        """
        for label in labels:
            self.add_label(label)

    def remove_label(self, label: str):
        """Removes label from the set of labels.

        params:
            str: The label to remove.
        returns:
            bool: Whether or not the item was successfully removed.
                  "False" if the item was not in the set.
        """
        try:
            self.labels.remove(label)
        except KeyError as e:
            print(f"Failed to remove label {label} from {self.labels}")
            return False
        return True

    def remove_labels(self, labels: list[str]):
        """Removes label from the set of labels.

        params:
            list[str]: The list of labels to remove.
        returns:
            bool: Whether or not the items were successfully removed.
                  "False" if any item was not in the set.
        """
        result = True
        for label in labels:
            result = result and self.remove_label(label)
        return result

    def change_time(self, new_time=None, new_duration=None):
        if new_time:
            self.start_time = new_time
        if new_duration:
            self.duration = new_duration
