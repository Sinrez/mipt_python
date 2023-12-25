"""
Пользователь - имеет логин и пароль, а так же календарь.
у пользователя есть итендифекатор начинающийся с @
"""

from hashlib import sha256

class User:
    def __init__(self, username, password):
        self.username = username
        self.password_hash = self.hash_password(password)
        self.calendars = []

    def create_calendar(self):
        # Реализация создания календаря для пользователя
        pass

    def authenticate(self, password):
        # Реализация аутентификации пользователя
        pass

    def create_event(self, calendar_id, event_data):
        # Реализация создания события пользователем
        pass

    def delete_event(self, event_id):
        # Реализация удаления события пользователем
        pass

    @staticmethod
    def hash_password(password):
        # Хеширование пароля
        return sha256(password.encode()).hexdigest()