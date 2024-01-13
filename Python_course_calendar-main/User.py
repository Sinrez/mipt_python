"""
Пользователь - имеет логин и пароль, а так же календарь.
у пользователя есть итендифекатор начинающийся с @
"""

from hashlib import sha256
from uuid import uuid4
from Backend import Backend

class User:
    def __init__(self, backend, username, password):
        self.backend = backend
        self.user_id = '@'+str(uuid4())  # Используем строковое представление UUID
        self.username = username
        self.password_hash = self.hash_password(password)
        self.calendars = []
        self.save_to_database()

    def authenticate(self, password):
        return self.password_hash == self.hash_password(password)

    @staticmethod
    def hash_password(password):
        return sha256(password.encode()).hexdigest()

    def save_to_database(self):
        user_data = {"username": self.username, "password_hash": self.password_hash}
        self.backend.users[self.user_id] = user_data
        self.backend.save_data_to_database()

        # Сохраняем календарь пользователя
        # calendar_id = len(self.calendars) + 1
        # calendar_data = {"user_id": self.user_id}
        # self.backend.calendars[calendar_id] = calendar_data
        # self.backend.save_data_to_database()

    @classmethod
    def load_from_database(cls, backend, user_id):
        user_data = backend.users.get(user_id)
        if user_data:
            loaded_user = cls(backend, username=user_data["username"], password="")
            loaded_user.load_calendars_from_database()
            return loaded_user
        return None

    def load_calendars_from_database(self):
        calendar_ids = [calendar_id for calendar_id, data in self.backend.calendars.items() if data["user_id"] == self.user_id]
        self.calendars = calendar_ids
