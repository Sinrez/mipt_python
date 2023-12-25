"""
Сущность, отвечающая за храние и предоставление данных
Оно хранит пользователей, календари и события.
Хранение в том числе означает сохранение между сессиями в csv файлах
(пароли пользователей хранятся как hash)

Должен быть статическим или Синглтоном

*) Нужно хранить для каждого пользователя все события которые с нима произошли но ещё не были обработаны.
"""
import csv
# from sq

class Backend:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Backend, cls).__new__(cls)
            # Инициализация данных
            cls._instance.users = {}
            cls._instance.calendars = {}
            cls._instance.events = {}
            cls._instance.pending_events = {}
        return cls._instance

    def save_data_to_csv(self, filename="data.csv"):
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            # Сохранение данных пользователей
            for user_id, user_data in self.users.items():
                writer.writerow(["user", user_id, user_data["username"], user_data["password_hash"]])

            # Сохранение данных календарей
            for calendar_id, calendar_data in self.calendars.items():
                writer.writerow(["calendar", calendar_id, calendar_data["user_id"]])

            # Сохранение данных событий
            for event_id, event_data in self.events.items():
                writer.writerow(["event", event_id, event_data["title"], event_data["description"],
                                event_data["start_time"], event_data["end_time"], event_data["organizer_id"]])

            # Сохранение данных ожидающих событий
            for user_id, pending_events in self.pending_events.items():
                for event_id in pending_events:
                    writer.writerow(["pending_event", user_id, event_id])

    def load_data_from_csv(self, filename="data.csv"):
        with open(filename, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == "user":
                    _, user_id, username, password_hash = row
                    self.users[user_id] = {"username": username, "password_hash": password_hash}
                elif row[0] == "calendar":
                    _, calendar_id, user_id = row
                    self.calendars[calendar_id] = {"user_id": user_id}
                elif row[0] == "event":
                    _, event_id, title, description, start_time, end_time, organizer_id = row
                    self.events[event_id] = {"title": title, "description": description,
                                            "start_time": start_time, "end_time": end_time,
                                            "organizer_id": organizer_id}
                elif row[0] == "pending_event":
                    _, user_id, event_id = row
                    if user_id not in self.pending_events:
                        self.pending_events[user_id] = []
                    self.pending_events[user_id].append(event_id)
