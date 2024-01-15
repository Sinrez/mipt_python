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

    # def __init__(self, user_id):
    #     self.user_id = user_id
    #     self.events = []

    def add_event(self, event):
        self.events.append(event)
    
    def get_events(self):
        print(f'События пользователя {self.user_id}')
        for ev in self.events:
            print(ev) 

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

#локальная проверка
# if __name__ == '__main__':
#     from datetime import datetime
#     from Event import Event
#     from User import User

#     user1 = User('Bob2', '12')
#     user1_id = user1.get_user_id()
#     event1 = Event("New Year's Eve Party", datetime(2023, 12, 31, 22, 0),datetime(2023, 12, 31, 22, 0), "Town Hall", user1)
#     event2 = Event("New Year's Eve Party", datetime(2024, 12, 31, 22, 0),datetime(2024, 12, 31, 22, 0), "Town Hall", user1)
#     event3 = Event("New Year's Eve Party", datetime(2023, 11, 11, 22, 0),datetime(2023, 11, 12, 22, 0), "Town Hall", user1)
#     calendar1 = Calendar(user1_id)
#     calendar1.add_event(event1)
#     calendar1.add_event(event2)
#     calendar1.add_event(event3)
#     calendar1.get_events()

#     # Удаление события
#     if event_id:= calendar1.remove_event(event3.get_event_id()):
#         print(f"Event {event_id} removed successfully")