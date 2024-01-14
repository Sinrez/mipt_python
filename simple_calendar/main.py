from datetime import datetime

class Event:
    """Class representing a New Year event with details."""
    def __init__(self, name, date, location):
        self.name = name
        self.date = date
        self.location = location

    def __str__(self):
        return f"{self.name} on {self.date.strftime('%Y-%m-%d %H:%M')} at {self.location}"

class EventManager:
    """Class managing a list of events."""
    def __init__(self):
        self.events = []

    def add_event(self, event):
        self.events.append(event)

    def display_events(self):
        for event in self.events:
            print(event)

    def get_events_by_date(self, date):
        return [event for event in self.events if event.date.date() == date]

# Example usage
event_manager = EventManager()
event_manager.add_event(Event("New Year's Eve Party", datetime(2023, 12, 31, 22, 0), "Town Hall"))
event_manager.add_event(Event("New Year's Concert", datetime(2023, 12, 31, 19, 0), "Central Park"))
event_manager.add_event(Event("Fireworks Show", datetime(2024, 1, 1, 0, 15), "River Side"))

# Display all events
print("Scheduled New Year Events:")
event_manager.display_events()

# Get events on a specific date
date_to_filter = datetime(2023, 12, 31).date()
print(f"\nEvents on {date_to_filter}:")
for event in event_manager.get_events_by_date(date_to_filter):
    print(event)