"""
Класс календаря - хранит события.
он умеет искать все события из промежутка (в том числе повторяющиеся)
он умеет добавлять/удалять события.
У каждого календаря ровно один пользователь.
"""
from Backend import Backend

class Calendar:
    def __init__(self, backend, user_id):
        self.backend = backend
        self.user_id = user_id
        self.events = []

    def add_event(self, event_id, title, description, start_time, end_time):
        #event_id будем получить из класса Event
        event_data = {
            "title": title,
            "description": description,
            "start_time": start_time,
            "end_time": end_time,
            "organizer_id": self.user_id
        }
        self.backend.events[event_id] = event_data
        self.events.append(event_id)
        return event_id

    def remove_event(self, event_id):
        if event_id in self.events:
            self.backend.events.pop(event_id)
            self.events.remove(event_id)
            return True
        return False

    def search_events(self, start_date, end_date):
        result = []
        for event_id in self.events:
            event_data = self.backend.events.get(event_id)
            if event_data and start_date <= event_data["start_time"] <= end_date:
                result.append(event_data)
        return result

# Пример использования:
backend_instance = Backend()
calendar_instance = Calendar(backend_instance, user_id=1)

# Добавление события
event_id = calendar_instance.add_event("Meeting", "Team meeting", "2023-01-01 10:00", "2023-01-01 11:00")

# Удаление события
# if calendar_instance.remove_event(event_id):
#     print(f"Event {event_id} removed successfully")

# Поиск событий в промежутке
events_in_range = calendar_instance.search_events("2023-01-01 00:00", "2023-01-02 00:00")
print("Events in range:", events_in_range)
