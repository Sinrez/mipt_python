"""
Пользователь - имеет логин и пароль, а так же календарь.
у пользователя есть итендифекатор начинающийся с @
"""

from hashlib import sha256
from uuid import uuid4

class User:
    def __init__(self, username, password):
        self.username = username
        self.password_hash = self.hash_password(password)
        self.calendars = []

    def authenticate(self, password):
        # Реализация аутентификации пользователя
        pass

    @staticmethod
    def hash_password(password):
        # Хеширование пароля
        return sha256(password.encode()).hexdigest()